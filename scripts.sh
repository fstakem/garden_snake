#!/usr/bin/env bash

# Micropython instructions
# ---------------------------------------------------------------------------------------------
# Find port of board
dmesg | grep ttyUSB

# Run: pyboard shows up on ttyACM0
rshell --port /dev/ttyUSB0 --baud 115200 --buffer-size 128 --editor nano
sudo ~/envs/upy_env/bin/rshell --port /dev/ttyUSB0 --baud 115200 --buffer-size 128 --editor vim

# Copy files to board filesystem
cp ./pycam/arducam.py /pyboard/arducam.py
cp ./pycam/arducam_constants.py /pyboard/arducam_constants.py
cp ./pycam/main.py /pyboard/main.py

# Flash new firmware with esptool: each board is slightly different
sudo ~/envs/upy_env/bin/esptool.py --port /dev/ttyUSB0 erase_flash
sudo ~/envs/upy_env/bin/esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 <firmmware_path>
sudo ~/envs/upy_env/bin/esptool.py --chip esp8266 --p /dev/ttyUSB0 write_flash --flash_size=detect 0 <firmmware_path>

# In rshell
ls /pyboard

# Start shell
shell



# Other
# ---------------------------------------------------------------------------------------------
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

# Equivalent to docker compose with individual containers
sudo docker run -it -h broker --name mqtt_broker -p 1883:1883 --rm eclipse-mosquitto
sudo docker run -it -h postgres --name db --rm -p 6000:5432 -e POSTGRES_PASSWORD=iotwin -d postgres
sudo docker run -it -h nodered --name nodered -p 1880:1880 --rm  nodered/node-red-docker
sudo docker run -it -h edge_agent --name edge_agent -p 5000:5000 --rm --env-file ./env_vars.sh edge_agent_img

# Remove all stopped containers
sudo docker rm -f $(sudo docker ps -a -q)


# Docker compose instructions
# ---------------------------------------------------------------------------------------------
# Remove all stopped containers
sudo docker rm -f $(sudo docker ps -a -q)

# Prune volumes if starting over and don't want db data
sudo docker volume prune

# Prune networks if they have changed and want to remove old ones
sudo docker network prune

# get containers up and running
sudo docker-compose up

# connect into db to do maintanace or add db
sudo docker run -it --rm --net garden_snake_back_net --link db:postgres postgres psql -h postgres -U postgres

# show er for db
eralchemy -i 'postgresql+psycopg2://postgres:iotwin@db:5432/iot_data' -o db.pdf

# get db IP or simply use hostname
sudo docker inspect db | grep IP

# connect to edge agent to run migration
sudo docker exec -it  -u 0 edge_agent /bin/bash
cd /opt/edge_agent/edge_agent/db
<source env vars postgres from project: 
    1) not in the container as didnt copy over \
    2) change host to proper host 
    3) port is 5432>
alembic upgrade head
exit



# Insert into db
insert into sample(data) values ('{"fred": "cool"}');
