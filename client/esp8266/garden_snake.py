# Sensors
#   1.  dfrobot capacitive moisture sensor v1.0
#   2.  dht22 temperature sensor

# Available GPIO
# 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16

from network import WLAN, STA_IF
from machine import ADC, Pin
from dht import DHT22
from mqtt_client import MQTTClient, MQTTException
from time import sleep
import ujson as json


# Globals
# ======================| START |======================|
CONFIG_PATH = '/config.json'
CMD_MSG_RCVD = False
# ======================| END |======================|


def load_config(path):
    config = None

    try:
        with open(path) as f:
            config = json.loads(f.read())
    except (OSError, ValueError):
        print("Could not load " + path)

    diff = config['sensors']['max_moisture'] - config['sensors']['min_moisture']
    config['sensors']['diff_moisture'] = diff

    if config:
        save_config(config, path)

    return config

def save_config(config, path):
    try:
        with open(path, "w") as f:
            f.write(json.dumps(config))
    except OSError:
        print("Couldn't save " + path)

def connect_wifi(name, passwd):
    wlan = WLAN(STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(name, passwd)

        while not wlan.isconnected():
            pass

    print('Connected with config:', wlan.ifconfig())

def mqtt_connect(name, ip):
    client = MQTTClient(name, ip)
    client.connect()

    return client

def setup(moisture_pin_num, temp_humid_pin_num):
    moisture_pin = ADC(moisture_pin_num)
    temp_humid_pin = DHT22(Pin(temp_humid_pin_num))

    return (moisture_pin, temp_humid_pin)

def get_moisture_data(moisture_pin, min_reading, reading_range):
    
    moisture_reading = moisture_pin.read()
    pct_dry = ((moisture_reading - min_reading) / reading_range) * 100

    return pct_dry

def get_temp_humid_data(temp_humid_pin):
    temp_humid_pin.measure()
    temp_c = temp_humid_pin.temperature() # eg. 23 (°C)
    temp_f = temp_c * 1.8 + 32 
    humid = temp_humid_pin.humidity()    # eg. 41 (% RH)

    return (temp_f, humid)

def create_msg(id, pct_dry, temp, humid):
    msg = {}
    msg['id'] = id
    msg['percent_dry'] = pct_dry
    msg['temperature'] = temp
    msg['humid'] = humid
    msg_bytes = bytes(str(msg), 'utf-8')

    return msg_bytes

def handle_msg(topic, msg):
    CMD_MSG_RCVD = False
    print(topic, msg)

def setup(config):
    # wifi
    name = config['board']['moisture_pin_num']
    passwd = config['board']['moisture_pin_num']
    connect_wifi(name, passwd)

    # sensors
    moisture_pin = ADC(config['board']['moisture_pin_num'])
    pin = Pin(config['board']['temp_humid_pin_num'])
    temp_humid_pin = DHT22(pin)

    return (moisture_pin, temp_humid_pin)

def run(config, moisture_pin, temp_humid_pin):
    mqtt_enabled = config['mqtt']['enabled']
    client = None

    try:
        # moisture sensor
        min_reading = config['sensors']['min_moisture']
        reading_range = config['sensors']['diff_moisture']
        pct_dry = get_moisture_data(moisture_pin, min_reading, reading_range)

        # temp/humid sensor
        temp, humid = get_temp_humid_data(temp_humid_pin)

        # mqtt
        id = config['mqtt']['id']
        
        msg = create_msg(id, pct_dry, temp, humid)
        print(msg)

        if mqtt_enabled:
            print('Publishing...')
            ip = config['mqtt']['ip']
            data_topic = bytes(config['mqtt']['data_topic'], 'utf-8')
            cmd_topic = bytes(config['mqtt']['cmd_topic'], 'utf-8')
            wait_time_sec = config['mqtt']['wait_time_sec']

            client = mqtt_connect(id, ip)
            client.set_callback(handle_msg)
            client.subscribe(cmd_topic)
            client.publish(data_topic, msg)

            seconds_waited = 0
            CMD_MSG_RCVD = False

            while seconds_waited < wait_time_sec:
                client.check_msg()

                if CMD_MSG_RCVD:
                    break

                sleep(1)
        
    except OSError:
        print('Reading error')
    except MQTTException:
        print('Mqtt error')

    if client:
        client.disconnect()

def main():
    config = load_config(CONFIG_PATH)

    if config:
        moisture_pin, temp_humid_pin = setup(config)

        # debug
        i = 0

        while True:
            run(config, moisture_pin, temp_humid_pin)
            sleep(config['runtime']['sleep_time_sec'])

            # debug
            i += 1
            if i > 5:
                break

    