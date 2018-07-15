# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from edge_agent.db.models.collector import Collector
from edge_agent.database import sql_db as db
from sqlalchemy.dialects.postgresql.json import JSONB


class Sensor(Collector):
    
    # Properties
    id = db.Column(db.Integer, db.ForeignKey('collector.id'), primary_key=True)
    sensor_board_id = db.Column(db.Integer, db.ForeignKey('sensor_board.id'))
    sensor_model_id = db.Column(db.Integer, db.ForeignKey('sensor_model.id'))
    calibration = db.Column(JSONB)

    # Relationships
    board = db.relationship("SensorBoard", back_populates="sensors")
    model = db.relationship("SensorModel", back_populates="sensors")

    __tablename__ = 'sensor'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)