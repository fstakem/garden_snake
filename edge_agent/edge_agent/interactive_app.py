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
from edge_agent.db.models.cloud_var import CloudVar
from edge_agent.db.models.collector import Collector
from edge_agent.db.models.device import Device
from edge_agent.db.models.gateway import Gateway
from edge_agent.db.models.installed_app import InstalledApp
from edge_agent.db.models.link import Link
from edge_agent.db.models.measurement import Measurement
from edge_agent.db.models.sample import Sample
from edge_agent.db.models.sensor import Sensor
from edge_agent.db.models.sensor_board import SensorBoard
from edge_agent.db.models.sensor_model import SensorModel

# Helper functions
def create_garden_collector(session):
    name = 'cheap humidity'
    meas_type = 'absolute humidity'
    description = 'A cheap air humidity measurement'
    units = 'gram per cubic meter'
    humid_meas = Measurement(name=name, measurement_type=meas_type, description=description, units=units)

    name = 'cheap temperature'
    meas_type = 'temperature'
    description = 'A cheap air temperature measurement'
    units = 'farenheit'
    temp_meas = Measurement(name=name,  measurement_type=meas_type, description=description, units=units)

    name = 'cheap soil dampness'
    meas_type = 'percent dry'
    description = 'A cheap soil dampness measurement'
    units = 'percent'
    soil_moist_meas = Measurement(name=name,  measurement_type=meas_type, description=description, units=units)

    name = 'cheap temp/humid sensor'
    model = 'dht22'
    temp_humid_model = SensorModel(name=name, model=model)
    temp_humid_model.measurements.append(humid_meas)
    temp_humid_model.measurements.append(temp_meas)

    temp_humid_sensor = Sensor()
    temp_humid_sensor.model = temp_humid_model

    name = 'cheap soil sensor'
    model = 'SEN0193'
    soil_model = SensorModel(name=name, model=model)
    soil_model.measurements.append(soil_moist_meas)

    soil_sensor = Sensor()
    soil_sensor.model = temp_humid_model

    device_id = str(uuid.uuid4())
    name = 'garden sensor'
    description = 'Sensor to collect data from the garden'
    version = '1_0_0'
    sensor_board = SensorBoard(device_id=device_id, name=name, description=description, version=version)
    sensor_board.sensors.append(temp_humid_sensor)
    sensor_board.sensors.append(soil_sensor)


    session.add(humid_meas)
    session.add(temp_meas)
    session.add(soil_moist_meas)
    session.add(temp_humid_model)
    session.add(soil_model)
    session.add(temp_humid_sensor)
    session.add(soil_sensor)
    session.add(sensor_board)

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
