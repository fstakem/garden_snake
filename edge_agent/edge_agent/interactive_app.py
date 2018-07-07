# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.11.18  
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import json
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
def load_fixtures(fixture_path):
    with open(fixture_path) as f:
        data = json.load(f)

    models = {}

    for m in data['sensor_models']:
        model = SensorModel(name=m['name'], model=m['model'], measurement_type=m['meas_type'], description=m['description'], units=m['units'])
        models[m['id']] = model
        session.add(model)

    for b in data['boards']:
        board = SensorBoard(uuid=b['id'], name=b['name'], description=b['description'], version=b['version'])
        print('Board uuid: {}'.format(b['id']))

        for s in b['sensors']:
            sensor = Sensor(uuid=s['id'])
            print('Sensor uuid: {}'.format(s['id']))

            sensor.model = models[s['model_id']]
            board.sensors.append(sensor)
            session.add(sensor)

        session.add(board)

    for c in data['cloud_sources']:
        cloud = CloudSource(uuid=c['id'], url=c['url'], name=c['name'], description=c['description'])
        print('Cloud uuid: {}'.format(c['id']))

        session.add(cloud)

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
fixture_path = '/home/fstakem/projects/garden_snake/edge_agent/edge_agent/fixtures/garden_6_30_18.json'

ipdb.set_trace()

# Example
# sample = Sample()
# session.add(sample)
# session.commit()
