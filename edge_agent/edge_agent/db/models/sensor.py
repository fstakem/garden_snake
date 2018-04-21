# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from .db.models.base_model import BaseModel
from .database import sql_db as db


class Sensor(BaseModel):
    
    # Properties
    collector_id = db.Column(db.Integer, db.ForeignKey('collector_id'), primary_key=True)
    sensor_model_id = db.Column(db.Integer, db.ForeignKey('sensor_model_id'), primary_key=True)
    connection_time = db.Column(db.DateTime, default=datetime.now)
    connected = db.Column(db.Boolean)
    collecting_data = db.Column(db.Boolean)

    # Relationships
    collector = relationship("Collector", back_populates="sensor_models")
    sensor_model = relationship("SensorModel", back_populates="collectors")

    __tablename__ = 'sensors'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)