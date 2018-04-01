# Sensors
#   1.  dfrobot capacitive moisture sensor v1.0
#   2.  dht22 temperature sensor

# Available GPIO
# 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16

from network import WLAN, STA_IF
from machine import ADC, Pin
from dht import DHT22
from urequests import post

# Config
MIN_MOISTURE = 404
MAX_MOISTURE = 776
DIFF_MOISTURE = MAX_MOISTURE - MIN_MOISTURE
DATA_URL = 'http://server/node/1/data'

MOISTURE_PIN_NUM = 0
TEMP_HUMID_PIN_NUM = 4

# Globals
moisture_pin = None
temp_humid_pin = None


def do_connect(name, passwd):
    wlan = WLAN(STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(name, passwd)

        while not wlan.isconnected():
            pass

    print('Connected with config:', wlan.ifconfig())

def setup():
    moisture_pin = ADC(MOISTURE_PIN_NUM)
    temp_humid_pin = DHT22(Pin(TEMP_HUMID_PIN_NUM))

def get_moisture_data():
    moisture_reading = moisture_pin.read()
    pct_wet = ((moisture_reading - MIN_MOISTURE) / DIFF_MOISTURE) * 100

    return pct_wet

def get_temp_humid_data():
    temp_humid_pin.measure()
    temp = temp_humid_pin.temperature() # eg. 23 (°C)
    humid = temp_humid_pin.humidity()    # eg. 41 (% RH)

    return (temp, humid)

def create_msg(pct_wet, temp, humid):
    msg = {}
    msg['percent_wet'] = pct_wet
    msg['temperature'] = temp
    msg['humid'] = humid

    return msg

def main():
    setup()

    pct_wet = get_moisture_data()
    temp, humid = get_temp_humid_data()
    msg = create_msg(pct_wet, temp, humid)

    response = post(DATA_URL, json=msg)
    return_msg = response.json()