# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from sqlalchemy.dialects.postgresql.json import JSONB

from edge_agent.db.models.base_model import BaseModel
from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db


class Collector(BaseModel, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True)
    type = db.Column(db.String)

    # Relationships
    samples = db.relationship("Sample", back_populates="collector")

    __tablename__ = 'collector'

    __mapper_args__ = {
        'polymorphic_identity':'collector',
        'polymorphic_on': type
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)