FROM python:3.6.5-slim-stretch

RUN apt-get update -y
RUN apt-get dist-upgrade -y

# Env vars
ENV USER=edge_agent \
    HOME=/home/edge_agent \
    TERM=xterm-256color \
    SERVER_ROOT_PATH=/opt/edge_agent \
    SERVER_APP_PATH=/opt/edge_agent/edge_agent \
    SETUP_PATH=/opt/edge_agent/setup

# Setup box
RUN mkdir -p $SETUP_PATH
COPY ./install_scripts/ $SETUP_PATH
COPY ./requirements.txt $SETUP_PATH
COPY ./edge_agent/ $SERVER_APP_PATH

# Install libs
RUN pip install -r $SETUP_PATH/requirements.txt

# Setup user
RUN useradd -ms /bin/bash -G sudo $USER
RUN chown $USER:$USER -R $SERVER_ROOT_PATH

USER edge_agent

# Finish
WORKDIR /opt/edge_agent

# debug
# CMD ["/bin/bash"]

CMD ["flask", "run", "--host=0.0.0.0"]