# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.11.18  
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
from pathlib import Path
import sys
import ipdb
from random import normalvariate
import uuid
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#import app
from edge_agent.database import sql_db

# Models
from edge_agent.db.models.app import App
from edge_agent.db.models.cloud_source import CloudSource
from edge_agent.db.models.collector import Collector
from edge_agent.db.models.device import Device
from edge_agent.db.models.gateway import Gateway
from edge_agent.db.models.installed_app import InstalledApp
from edge_agent.db.models.link import Link
from edge_agent.db.models.sample import Sample
from edge_agent.db.models.sensor import Sensor
from edge_agent.db.models.sensor_board import SensorBoard
from edge_agent.db.models.sensor_model import SensorModel

# Helper functions
def create_garden_collector(session):

    # Temperature
    name = 'cheap temp sensor'
    model = 'dht22'
    meas_type = 'temperature'
    description = 'A cheap air temperature measurement'
    units = 'farenheit'
    temp_model = SensorModel(name=name, model=model, measurement_type=meas_type, description=description, units=units)

    uuid_str = str(uuid.uuid4())
    temp_sensor = Sensor(uuid=uuid_str)
    temp_sensor.model = temp_model
    print('Temp uuid: {}'.format(uuid_str))

    # Humidity
    name = 'cheap humidity sensor'
    model = 'dht22'
    meas_type = 'humidity'
    description = 'A cheap air humidity measurement'
    units = 'gram per cubic meter'
    humid_model = SensorModel(name=name, model=model, measurement_type=meas_type, description=description, units=units)

    uuid_str = str(uuid.uuid4())
    humid_sensor = Sensor(uuid=uuid_str)
    humid_sensor.model = humid_model
    print('Humid uuid: {}'.format(uuid_str))

    # Soil dryness
    name = 'cheap soil sensor'
    model = 'SEN0193'
    meas_type = 'percent dry'
    description = 'A cheap soil dampness measurement'
    units = 'percent'
    soil_model = SensorModel(name=name, model=model, measurement_type=meas_type, description=description, units=units)

    uuid_str = str(uuid.uuid4())
    soil_sensor = Sensor(uuid=uuid_str)
    soil_sensor.model = soil_model
    print('Soil sensor uuid: {}'.format(uuid_str))

    # Board
    uuid_str = str(uuid.uuid4())
    name = 'garden sensor'
    description = 'Sensor to collect data from the garden'
    version = '1_0_0'
    sensor_board = SensorBoard(uuid=uuid_str, name=name, description=description, version=version)
    sensor_board.sensors.append(temp_sensor)
    sensor_board.sensors.append(humid_sensor)
    sensor_board.sensors.append(soil_sensor)
    print('Board uuid: {}'.format(uuid_str))

    uuid_str = str(uuid.uuid4())
    url = 'http://api.wunderground.com/api'
    name = 'wunderground'
    description = 'Weather underground atlanta weather'
    cloud_source = CloudSource(uuid=uuid_str, url=url, name=name, description=description)
    print('Wunderground uuid: {}'.format(uuid_str))

    session.add(temp_model)
    session.add(humid_model)
    session.add(soil_model)
    session.add(temp_sensor)
    session.add(humid_sensor)
    session.add(soil_sensor)
    session.add(sensor_board)
    session.add(cloud_source)

    session.commit()

def create_random_sample(data_vars=None, collector=None):
    if not data_vars:
        data_vars = ['x', 'y', 'z']

    data = {x:normalvariate(50, 20) for x in data_vars}
    sample = Sample(data=data)

    if collector:
        sample.collector = collector

    return sample

from edge_agent.config.config import load_config

app_config = load_config()

db_str = app_config['db_connect_str']
engine = create_engine(db_str)
Session = sessionmaker(bind=engine)
session = Session()

ipdb.set_trace()

# Example
# sample = Sample()
# session.add(sample)
# session.commit()
