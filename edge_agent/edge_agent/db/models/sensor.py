# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from .base_model import BaseModel
from ...database import sql_db as db


class Sensor(BaseModel):
    
    # Properties
    collector_id = db.Column(db.Integer, db.ForeignKey('collector.id'), primary_key=True)
    sensor_model_id = db.Column(db.Integer, db.ForeignKey('sensor_model.id'), primary_key=True)
    connection_time = db.Column(db.DateTime, default=datetime.now)
    connected = db.Column(db.Boolean)
    collecting_data = db.Column(db.Boolean)

    # Relationships
    collector = db.relationship("Collector", back_populates="sensor_models")
    sensor_model = db.relationship("SensorModel", back_populates="collectors")

    __tablename__ = 'sensor'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)