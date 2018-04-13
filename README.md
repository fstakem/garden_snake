Garden sensors with sensor, edge, and cloud components

1. The only client currently supported is the classic ESP 8266
2. The client code is in micropython and will likely be ported to ESP 32
3. The edge has a few simepl components: mqtt broker, postgres, edge agent, and node red
4. Currently the processing pipeline is done with nodered
5. Node red is eating all the RAM on the pi so will likely move to a rock64 and own custom pipeline
6. The data will be stored in postgres on the edge to save money from cloud hosting
7. Redis support is planned on the edge
8. The edge agent will have a basic restful interface to the data with sqlalchemy and flask
9. The cloud component is likely to be done last and is not an important part of this project
10. The current sensors supported are ground moisture, temperature, and humidity
11. The temperature and humidty sensor will likely be upgraded from the cheap dht22 to something more robust
