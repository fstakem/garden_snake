Garden sensors with sensor, edge, and cloud components

1. The only client currently supported is the classic ESP 8266
2. The client code is in micropython and will likely be ported to ESP 32
3. The edge has a few simple components: mqtt broker, postgres, edge agent, and node red
4. Currently the processing pipeline is done with nodered
5. Node red is eating all the RAM on the pi so will likely move to a rock64 and own custom pipeline
6. The data will be stored in postgres on the edge to save money from cloud hosting
7. Redis support is planned on the edge for short timeseries data store
8. The edge agent will have a basic restful interface to the data with sqlalchemy and flask
9. The cloud component is likely to be done last and is not an important part of this project
10. The current sensors supported are ground moisture, temperature, and humidity
11. The temperature and humidty sensor will likely be upgraded from the cheap dht22 to something more robust
12. Flask microservice architecture could be redone so that versioning is done on the webserver not the app
13. Flask is using internal web server for the time being as data volume is low
14. Need to figure out an automated way to update node red and install DAG
15. Research on parsing nodered DAG and using in custom processing engine needs to be done
16. Clients need to switch to using coap instead of mqtt but micropython support is not great
17. High rate signals should not use something like mqtt
18. Sound sensors for higher rate data is also planned but client side work needs to be done

TODO
1. Add ability to export db to er diagram
2. Research node red use of functions, templates, db, requests
3. Create new tables for generic weather data
4. Redo tables for insert of raw samples
5. Finish node red flow for insertion
6. Setup new computer with docker and run the docker compose
7. Finish sensor hardware
8. Finish power supply hardware
9. Deploy system
10. Research new sensors and put together prototype
