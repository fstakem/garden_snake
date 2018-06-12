# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime
from edge_agent.db.models.base_model import BaseModel
from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db


class Link(BaseModel, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    gateway_id = db.Column(db.Integer, db.ForeignKey('gateway.id'))
    sensor_board_id = db.Column(db.Integer, db.ForeignKey('sensor_board.id'))
    local = db.Column(db.Boolean)
    last_contacted = db.Column(db.DateTime, default=datetime.now)
    collecting_data = db.Column(db.Boolean)
    max_msg_interval_sec = db.Column(db.Integer)

    # Relationships
    gateway = db.relationship("Gateway", back_populates="links")
    sensor_board = db.relationship("SensorBoard", back_populates="link")

    __tablename__ = 'link'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)