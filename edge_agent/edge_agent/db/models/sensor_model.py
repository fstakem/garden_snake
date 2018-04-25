# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.base_model import BaseModel
from edge_agent.database import sql_db as db


class SensorModel(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    model = db.Column(db.String)
    measurement_type = db.Column(db.String)
    description = db.Column(db.String)
    units = db.Column(db.String)

    # Relationships
    sensors = db.relationship("Sensor", back_populates="sensor_model")

    __tablename__ = 'sensor_model'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)