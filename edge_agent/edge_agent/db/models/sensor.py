# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.17.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from .db.models.base_model import BaseModel
from .database import sql_db as db


class Sensor(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, Sequence('sensor_id_seq'), primary_key=True)
    name = Column(String(50))

    # Constraints
    # TODO

    # Relationships
    # TODO

    __tablename__ = 'sensors'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)