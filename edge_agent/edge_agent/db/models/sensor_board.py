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


class SensorBoard(Device):
    
    # Properties
    id = db.Column(db.Integer, db.ForeignKey('device.id'), primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    version = db.Column(db.String)

    # Relationships
    sensors = db.relationship("Sensor", back_populates="sensor_board")
    link = db.relationship("Link", back_populates="sensor_board")

    __tablename__ = 'sensor_board'

    __mapper_args__ = {
        'polymorphic_identity': 'sensor_board',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)