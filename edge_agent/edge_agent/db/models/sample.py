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


class Sample(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    # Relationships
    sensor = db.relationship("Sensor", back_populates="samples")

    __tablename__ = 'sample'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)