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

import app
from edge_agent.database import sql_db

# Models
from edge_agent.db.models.app import App
from edge_agent.db.cloud_source import CloudSource
from edge_agent.db.cloud_var import CloudVar
from edge_agent.db.collector import Collector
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
    uuid_str = str(uuid.uuid4())
    name = 'garden_sensor_1'
    collector = Collector(device_id=uuid_str, name=name)

    name = 'cheap temp sensor'
    model = 'dht22'
    measurement_type = 'temp'
    description = 'A cheap temperature sensor'
    units = 'farenheit'
    temp_sensor_model = SensorModel(name=name, model=model, measurement_type=measurement_type, 
                                    description=description, units=units)

    name = 'cheap humid sensor'
    model = 'dht22'
    measurement_type = 'relative humid'
    description = 'A cheap humid sensor'
    units = 'percent'
    humid_sensor_model = SensorModel(name=name, model=model, measurement_type=measurement_type, 
                                     description=description, units=units)

    name = 'cheap moisture sensor'
    model = 'SEN0193'
    measurement_type = 'percent dry'
    description = 'A cheap moisture sensor'
    units = 'percent'
    water_sensor_model = SensorModel(name=name, model=model, measurement_type=measurement_type, 
                                     description=description, units=units)

    connection_time = datetime.utcnow()
    connected = True
    collecting_data = True
    temp_sensor = Sensor(connection_time=connection_time, connected=connected, 
                         collecting_data=collecting_data)

    connection_time = datetime.utcnow()
    connected = True
    collecting_data = True
    humid_sensor = Sensor(connection_time=connection_time, connected=connected, 
                          collecting_data=collecting_data)

    connection_time = datetime.utcnow()
    connected = True
    collecting_data = True
    water_sensor = Sensor(connection_time=connection_time, connected=connected, 
                          collecting_data=collecting_data)   

    humid_sensor_model.sensors.append(humid_sensor)
    temp_sensor_model.sensors.append(temp_sensor)
    water_sensor_model.sensors.append(water_sensor)

    collector.sensors.append(temp_sensor)
    collector.sensors.append(humid_sensor)
    collector.sensors.append(water_sensor)

    session.add(collector)
    session.add(temp_sensor_model)
    session.add(humid_sensor_model)
    session.add(water_sensor_model)
    session.add(temp_sensor)
    session.add(humid_sensor)
    session.add(water_sensor)

    session.commit()

def create_random_sample(data_vars=None):
    if not data_vars:
        data_vars = ['x', 'y', 'z']

    data = {x:normalvariate(50, 20) for x in data_vars}
    sample = Sample(data=data)

    return sample


db_str = app.app_config['db_connect_str']
engine = create_engine(db_str)
Session = sessionmaker(bind=engine)
session = Session()

ipdb.set_trace()

# Example
# sample = Sample()
# session.add(sample)
# session.commit()
