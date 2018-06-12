# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.base_model import BaseModel
from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db


class CloudSource(BaseModel, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)

    # Relationships
    cloud_vars = db.relationship("CloudVar", back_populates="cloud_source")

    __tablename__ = 'cloud_source'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)