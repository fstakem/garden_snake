# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.12.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.base_model import BaseModel
from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db


class Measurement(BaseModel, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    sensor_model_id = db.Column(db.Integer, db.ForeignKey('sensor_model.id'))
    name = db.Column(db.String)
    description = db.Column(db.String)
    units = db.Column(db.String)

    # Relationships
    sensor_model = db.relationship("SensorModel", back_populates="measurements")

    __tablename__ = 'measurement'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)