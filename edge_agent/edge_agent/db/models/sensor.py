# Libraries
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Numeric

from micro_service.db.models.api import Base
from micro_service.db.models.base_model import BaseModel

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, Sequence('sensor_id_seq'), primary_key=True)
    name = Column(String(50))