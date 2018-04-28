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

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app
from edge_agent.database import sql_db

# Models
from edge_agent.db.models.app import App
from edge_agent.db.models.collector import Collector
from edge_agent.db.models.device import Device
from edge_agent.db.models.gateway import Gateway
from edge_agent.db.models.installed_app import InstalledApp
from edge_agent.db.models.sample import Sample
from edge_agent.db.models.sensor import Sensor
from edge_agent.db.models.sensor_model import SensorModel

# Helper functions
def create_base_system(session):
    device = Device()


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
