# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from edge_agent.db.models.base_model import BaseModel
from edge_agent.database import sql_db as db


class Sensor(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    collector_id = db.Column(db.Integer, db.ForeignKey('collector.id'))
    sensor_model_id = db.Column(db.Integer, db.ForeignKey('sensor_model.id'))
    connection_time = db.Column(db.DateTime, default=datetime.now)
    connected = db.Column(db.Boolean)
    collecting_data = db.Column(db.Boolean)

    # Relationships
    collector = db.relationship("Collector", back_populates="sensors")
    sensor_model = db.relationship("SensorModel", back_populates="sensors")
    samples = db.relationship("Sample", back_populates="sensor")

    __tablename__ = 'sensor'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)