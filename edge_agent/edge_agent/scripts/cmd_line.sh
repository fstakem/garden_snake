# Start postgres
sudo docker run --rm --name postgres_db -p 6000:5432 -e POSTGRES_PASSWORD=passwd -d postgres

# Connect to postgres docker through command line
sudo docker exec -it postgres_db bash
psql -U postgres

# Create db
CREATE DATABASE iot_data;

# Connect to postgres docker
psql -h localhost -p 6000 -U postgres

# Get postgres ip
sudo docker inspect postgres_db | grep IPAddress\"

# Build image
sudo docker build -t image_name --rm .

# Remove all related a container
sudo docker rmi -f image_name:latest

# Log into container as root and change password
docker exec -u 0 -it coap_srv_box bash
passwd coap

6ba1c3ac75dd
docker exec -u 0 -it 6ba1c3ac75dd bash

# Remove all containers
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)