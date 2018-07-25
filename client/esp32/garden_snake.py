import json
import network
from time import sleep

from machine import ADC, Pin

# LED pin 21
# led = Pin(21, Pin.OUT)
# led.value(1)


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

    return config.json


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

# Globals
# ======================| START |======================|
CONFIG_PATH = '/config.json'
config = load_config(CONFIG_PATH)
# ======================| END |======================|


def main():
    cap_moist_pin_num = 34
    cap_moist_pin = ADC(Pin(cap_moist_pin_num))
    cap_moist_pin.atten(ADC.ATTN_11DB)

    veg_moist_pin_num = 35
    veg_moist_pin = ADC(Pin(veg_moist_pin_num))
    veg_moist_pin.atten(ADC.ATTN_11DB)


from machine import ADC, Pin
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
