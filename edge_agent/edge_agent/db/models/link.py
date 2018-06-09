# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.base_model import BaseModel
from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db


class Link(BaseModel, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    gateway_id = db.Column(db.Integer, db.ForeignKey('gateway.id'))
    sensor_board_id = db.Column(db.Integer, db.ForeignKey('sensor_board.id'))
    local = db.Column(db.Boolean)

    # Relationships
    gateway = db.relationship("Gateway", back_populates="connections")
    sensor_board = db.relationship("SensorBoard", back_populates="connection")

    __tablename__ = 'link'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)