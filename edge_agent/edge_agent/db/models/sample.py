# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from .db.models.base_model import BaseModel
from .database import sql_db as db


class Sample(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, db.Sequence('sample_id_seq'), primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor_id'), primary_key=True)

    # Relationships
    sensor = relationship("Sensor", back_populates="samples")

    __tablename__ = 'samples'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)