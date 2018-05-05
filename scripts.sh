#!/usr/bin/env bash

# Find port of board
dmesg | grep ttyUSB

# Run: pyboard shows up on ttyACM0
rshell --port /dev/ttyUSB0 --baud 115200 --buffer-size 128 --editor nano
sudo ~/envs/upy_env/bin/rshell --port /dev/ttyUSB0 --baud 115200 --buffer-size 128 --editor vim

# Copy files
cp ./pycam/arducam.py /pyboard/arducam.py
cp ./pycam/arducam_constants.py /pyboard/arducam_constants.py
cp ./pycam/main.py /pyboard/main.py

# Flash new firmware with esptool
sudo ~/envs/upy_env/bin/esptool.py --port /dev/ttyUSB0 erase_flash
sudo ~/envs/upy_env/bin/esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 <firmmware_path>
sudo ~/envs/upy_env/bin/esptool.py --chip esp8266 --p /dev/ttyUSB0 write_flash --flash_size=detect 0 <firmmware_path>

# In rshell
ls /pyboard

# Start shell
shell

# Start mosquitto
sudo docker run -it -h broker --name mqtt_broker_box -p 1883:1883 --rm eclipse-mosquitto
sudo docker run -it -h broker --name mqtt_broker_box -p 1883:1883 --rm --restart always eclipse-mosquitto
sudo docker inspect mqtt_broker_box | grep IPAddress

# Pi mosquitto
git clone https://github.com/pascaldevink/rpi-mosquitto
sudo docker build --tag mosquitto .
sudo docker run -it -h broker --name mqtt_broker_box -p 1883:1883 --rm mosquitto
sudo docker run -ti -p 1883:1883 -p 9001:9001 \
-v /srv/mqtt/config:/mqtt/config:ro \
-v /srv/mqtt/log:/mqtt/log \
-v /srv/mqtt/data/:/mqtt/data/ \
--name mqtt_broker_box --rm mosquitto mosquitto 

# Pi postgres
# https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi
sudo apt install postgresql libpq-dev postgresql-client postgresql-client-common -y
sudo su postgres
createuser pi -P --interactive
    pw: iotwin
    n
    y
    y
db: iot_data

# Postgres for testing
sudo docker pull postgres:latest
sudo docker run -it -h postgres --name garden-postgres --rm -e POSTGRES_PASSWORD=iotwin -d postgres
sudo docker exec -it garden-postgres psql -U project -W project project
sudo docker run -it --rm --link garden_postgres:postgres postgres psql -h postgres -U postgres

# Install postgres additions to node red
cd /usr/lib/node_modules/node-red
sudo npm install node-red-contrib-postgres

# Start node red
node-red-start
