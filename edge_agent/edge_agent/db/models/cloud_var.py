# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge.db.models.collector import Collector
from edge_agent.database import sql_db as db


class CloudVar(Collector):
    
    # Properties
    id = db.Column(db.Integer, db.ForeignKey('collector.id'), primary_key=True)
    cloud_source_id = db.Column(db.Integer, db.ForeignKey('cloud_source.id'))
    name = db.Column(db.String)
    description = db.Column(db.String)
    units = db.Column(db.String)

    # Relationships
    cloud_source = db.relationship("CloudSource", back_populates="cloud_var")

    __tablename__ = 'cloud_param'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)