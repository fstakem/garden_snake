# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.db.models.base_model import BaseModel
from edge_agent.database import sql_db as db


class Device(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(36), nullable=False, unique=True)
    name = db.Column(db.String)
    type = db.Column(db.String)

    # Relationships
    installed_apps = db.relationship("InstalledApp", back_populates="device")

    __tablename__ = 'device'

    __mapper_args__ = {
        'polymorphic_identity':'device',
        'polymorphic_on':type
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def install_app(remove_old=True):
        pass