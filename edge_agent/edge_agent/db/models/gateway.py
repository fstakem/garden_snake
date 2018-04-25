# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.device import Device
from edge_agent.database import sql_db as db


class Gateway(Device):
    
    # Properties
    id = db.Column(db.Integer, db.ForeignKey('device.id'), primary_key=True)

    # Relationships
    #collectors = db.relationship("Collector", back_populates="gateway")

    __tablename__ = 'gateway'

    __mapper_args__ = {
        'polymorphic_identity': 'gateway',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)