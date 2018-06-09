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


class Sensor(Collector):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    sensor_board_id = db.Column(db.Integer, db.ForeignKey('sensor_board.id'))
    sensor_model_id = db.Column(db.Integer, db.ForeignKey('sensor_model.id'))
    connection_time = db.Column(db.DateTime, default=datetime.now)
    connected = db.Column(db.Boolean)
    collecting_data = db.Column(db.Boolean)

    # Relationships
    sensor_board = db.relationship("SensorBoard", back_populates="sensors")
    sensor_model = db.relationship("SensorModel", back_populates="sensors")

    __tablename__ = 'sensor'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)