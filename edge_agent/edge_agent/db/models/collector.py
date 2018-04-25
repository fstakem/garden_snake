# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.17.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.device import Device
from edge_agent.database import sql_db as db


class Collector(Device):
    
    # Properties
    id = db.Column(db.Integer, db.ForeignKey('device.id'), primary_key=True)
    #gateway_id = db.Column(db.Integer, db.ForeignKey('gateway.id'))

    # Relationships
    #gateway = db.relationship("Gateway", back_populates="collectors")
    sensors = db.relationship("Sensor", back_populates="collector")

    __tablename__ = 'collector'

    __mapper_args__ = {
        'polymorphic_identity': 'collector',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)