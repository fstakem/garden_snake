# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.database import sql_db as db

from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db
from sqlalchemy.dialects.postgresql.json import JSONB


class Sample(db.Model, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    collector_id = db.Column(db.Integer, db.ForeignKey('collector.id'))
    timestamp = db.Column(db.DateTime)
    data = db.Column(JSONB)

    # Relationships
    collector = db.relationship("Collector", back_populates="samples")

    __tablename__ = 'sample'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)