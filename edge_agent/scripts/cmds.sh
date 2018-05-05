# Run base container
sudo docker run -it -h agent --name edge_agent --rm python:3.6.5-slim-stretch

# Build container
sudo docker build --tag edge_agent_img .

# Run new container
sudo docker run -it -h edge_agent -p 5000:5000 --name edge_agent --rm --env-file ./env_vars.sh edge_agent_img