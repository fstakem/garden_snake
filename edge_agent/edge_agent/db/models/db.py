import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class SensorNode(Base):
    __tablename__ = 'sensor_nodes'

    id = Column(Integer, Sequence('sensor_node_id_seq'), primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "SensorNode(name='%s')" % (self.name)

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, Sequence('sensor_id_seq'), primary_key=True)
    name = Column(String(50))

class GardenSensor(Base):
    __tablename__ = 'garden_sensors'

class GardenSample(Base):
    __tablename__ = 'garden_samples'

    id = Column(Integer, Sequence('garden_sample_id_seq'), primary_key=True)