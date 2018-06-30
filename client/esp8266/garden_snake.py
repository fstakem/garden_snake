# Sensors
#   1.  dfrobot capacitive moisture sensor v1.0
#   2.  dht22 temperature sensor

# Available GPIO
# 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16

import network
import machine
from machine import ADC, Pin, freq
from ubinascii import hexlify
from dht import DHT22
from mqtt_client import MQTTClient, MQTTException
from time import sleep, time, localtime
import ujson as json
import ntptime


# Globals
# ======================| START |======================|
CONFIG_PATH = '/config.json'
CMD_MSG_RCVD = False
config = load_config(CONFIG_PATH)
# ======================| END |======================|


def load_config(path):
    config = None

    try:
        with open(path) as f:
            config = json.loads(f.read())
    except (OSError, ValueError):
        print("Could not load " + path)

    diff = config['sensors']['soil']['max_moisture'] - config['sensors']['soil']['min_moisture']
    config['sensors']['soil']['diff_moisture'] = diff

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
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print('Connecting to network...')

        if name and passwd:
            sta_if.connect(name, passwd)
        else:
            print('Using known network...')
            sleep(2)

        while not sta_if.isconnected():
            pass

    print('Connected with config:', sta_if.ifconfig())

def get_mac():
    mac = hexlify(network.WLAN().config('mac'),':').decode()
    
    return mac

def mqtt_connect(ip):
    client = MQTTClient(config['board']['id'], config['mqtt']['ip'])
    client.connect()

    return client

def setup(moisture_pin_num, temp_humid_pin_num):
    moisture_pin = ADC(moisture_pin_num)
    temp_humid_pin = DHT22(Pin(temp_humid_pin_num))

    return (moisture_pin, temp_humid_pin)

def get_moisture_data(moisture_pin):
    moisture_reading = moisture_pin.read()
    min_reading = config['sensors']['soil']['min_moisture']
    reading_range = config['sensors']['soil']['diff_moisture']
    pct_dry = ((moisture_reading - min_reading) / reading_range) * 100

    return pct_dry

def get_temp_humid_data(temp_humid_pin):
    temp_humid_pin.measure()
    temp_c = temp_humid_pin.temperature() # eg. 23 (°C)
    temp_f = temp_c * 1.8 + 32 
    humid = temp_humid_pin.humidity()    # eg. 41 (% RH)

    return (temp_f, humid)

def get_timestamp(update=False):
    if update:
        ntptime.settime()

    ts = localtime()
    timestamp_str = '{}-{}-{}T{}:{}:{}Z'.format(ts[0], ts[1], ts[2], ts[3], ts[4], ts[5])

    return timestamp_str

def create_msg(pct_dry, temp, humid):
    """
    Msg format:
    {
        "board_id": "9cf0bab7-d3e6-4a3e-a5fe-9dfde5edc842",
        "timestamp": "2018-06-12T01:45:30.250Z",
        "sensors": [
            {
                "sensor_id": "658ad87f-79f2-4c8c-9ae4-43a4a72f6253",
                "value": ".85",
                "type": "percent_dry"
            },
            {
                "sensor_id": "98258788-9fbb-44e5-85cd-f8d5723f379f",
                "value": "79.5",
                "type": "temperature"
            },
            {
                "sensor_id": "086975c5-623f-42ef-8620-7ff90d9bafd8",
                "value": "32",
                "type": "humidity"
            }
        ]
    }
    """
    msg = {}
    msg['board_id'] = config['board']['id']
    msg['timestamp'] = get_timestamp(True)
    msg['sensors'] = []

    sensor = {}
    sensor['sensor_id'] = config['sensors']['soil']['id']
    sensor['value'] = pct_dry
    sensor['type'] = 'percent_dry'
    msg['sensors'].append(sensor)

    sensor = {}
    sensor['sensor_id'] = config['sensors']['temp']['id']
    sensor['value'] = temp
    sensor['type'] = 'temperature'
    msg['sensors'].append(sensor)

    sensor = {}
    sensor['sensor_id'] = config['sensors']['humid']['id']
    sensor['value'] = humid
    sensor['type'] = 'humidity'
    msg['sensors'].append(sensor)

    msg_bytes = bytes(str(msg), 'utf-8')

    return msg_bytes

def handle_msg(topic, msg):
    CMD_MSG_RCVD = False
    print(topic, msg)

def setup():
    # wifi
    name = config['board']['moisture_pin_num']
    passwd = config['board']['moisture_pin_num']
    connect_wifi(name, passwd)

    # sensors
    moisture_pin = ADC(config['board']['moisture_pin_num'])
    pin = Pin(config['board']['temp_humid_pin_num'])
    temp_humid_pin = DHT22(pin)

    return (moisture_pin, temp_humid_pin)

def run(moisture_pin, temp_humid_pin):
    mqtt_enabled = config['mqtt']['enabled']

    if mqtt_enabled:
        data_topic = bytes(config['mqtt']['data_topic'], 'utf-8')
        cmd_topic = bytes(config['mqtt']['cmd_topic'], 'utf-8')
        wait_time_sec = config['mqtt']['wait_time_sec']

    client = None

    try:
        pct_dry = get_moisture_data(moisture_pin)
        temp, humid = get_temp_humid_data(temp_humid_pin)
        msg = create_msg(pct_dry, temp, humid)
        print(msg)

        if mqtt_enabled:
            print('Publishing...')
            client = mqtt_connect()
            client.set_callback(handle_msg)
            client.subscribe(cmd_topic)
            client.publish(data_topic, msg)

            start_time = time()
            seconds_waited = 0
            CMD_MSG_RCVD = False

            while True:
                current_time = time()
                seconds_waited = current_time - start_time

                if seconds_waited > wait_time_sec or wait_time_sec == 0:
                    break
                    
                print('Looking for command msg')
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
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print('Woke from a deep sleep...')

    debug = config['runtime']['debug']

    if config:
        moisture_pin, temp_humid_pin = setup()
        sleep_time = config['runtime']['sleep_time_sec']

        while True:
            start_time = time()
            run(moisture_pin, temp_humid_pin)
            elapsed_time = time() - start_time
            new_sleep_time = sleep_time - elapsed_time

            if debug:
                print('Debug...')
                if elapsed_time < sleep_time:
                    sleep(new_sleep_time)     
            else:
                rtc = machine.RTC()
                rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
                sleep_time_ms = 1000 * new_sleep_time
                rtc.alarm(rtc.ALARM0, sleep_time_ms)
                machine.deepsleep()

                   


    