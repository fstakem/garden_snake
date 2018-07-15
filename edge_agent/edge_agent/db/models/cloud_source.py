# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.collector import Collector
from edge_agent.database import sql_db as db


class CloudSource(Collector):
    
    # Properties
    id = db.Column(db.Integer, db.ForeignKey('collector.id'), primary_key=True)
    url = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)

    # Relationships

    __tablename__ = 'cloud_source'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)