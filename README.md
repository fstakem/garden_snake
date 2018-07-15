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

Setup for Ubuntu
1. Get containers up and running
  * Git clone repo
  * cd garden_snake/edge_agent
  * sudo docker build --tag edge_agent_img .
  * cd ..
  * sudo docker-compose up
2. Setup python with pyenv
  * git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  * echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  * echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  * echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  * exec "$SHELL"
  * sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
  * sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev
  * sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
  * sudo apt-get install libssl-dev openssl
  * sudo apt-get install libffi-dev
  * sudo apt-get install libreadline-gplv2-dev libbz2-dev
  * pyenv install 3.7.0
  * pyenv global 3.7.0
3. Run migrations
  * cd garden_snake/edge_agent
  * pip install virualenv
  * virtualenv edge_agent_env
  * source edge_agent_env/bin/activate
  * pip install -r requirements.txt
  * sudo docker inspect db | grep IPAddress
  * vim ./env_vars/postgres.sh
  * > In vim change ip to that found from docker inspect
  * vim ./env_vars/alembic_export.sh
  * > In vim change ip to that found from docker inspect
  * source source_env_vars.sh
  * cd edge_agent/db
  * alembic upgrade head
  * cd ../..
  * ./run_interactive_app.sh
  * > In ipython set path: fixture_path = '/home/fstakem/garden_snake/edge_agent/edge_agent/fixtures/garden_6_30_18.json'
  * > In ipython run function: load_fixtures(fixture_path)
  * quit() (to leave ipython)
4. Setup nodered
  * Navigate to web UI: http://king-cobra.local:1880/
  * Install components: node-red-contrib-postgres, node-red-node-weather-underground
  * Import both flows
  * Configure: wunderground -> api key
  * Configure both postgres passwords -> user and password
  * Deploy
