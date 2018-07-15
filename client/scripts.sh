# Micropython instructions
# ---------------------------------------------------------------------------------------------
# Find port of board
dmesg | grep ttyUSB

# Run: pyboard shows up on ttyACM0
sudo ~/envs/upy_env/bin/rshell --port /dev/ttyUSB0 --baud 115200 --buffer-size 128 --editor vim

# Copy files to board filesystem
cp ./filename.py /pyboard/filename.py

# Flash new firmware with esptool: each board is slightly different
sudo ~/envs/upy_env/bin/esptool.py --port /dev/ttyUSB0 erase_flash
sudo ~/envs/upy_env/bin/esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 <firmmware_path>
sudo ~/envs/upy_env/bin/esptool.py --chip esp8266 --p /dev/ttyUSB0 write_flash --flash_size=detect 0 <firmmware_path>

# In rshell
ls /pyboard

# Start shell
shell


# Setup wifi
# ---------------------------------------------------------------------------------------------
# Once in rshell start repl
repl

# Get network params
import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# turn on ability to access AP
sta_if.active(True)

# turn off local AP
ap_if.active(False)

sta_if.isconnected()
passwd = ''
sta_if.connect('edje_compute', passwd)

# Exit repl
ctrl-x