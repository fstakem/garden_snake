# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from .db.models.base_model import BaseModel
from .database import sql_db as db


class Device(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, db.Sequence('device_id_seq'), primary_key=True)
    device_id = db.Column(db.String(36), nullable=False, unique=True)
    name = db.Column(db.String)
    type = Column(String)

    # Relationships
    installed_apps = relationship("InstalledApp", back_populates="device")
    installed_app_history = relationship("InstalledAppHistory", back_populates="device")

    __tablename__ = 'devices'

    __mapper_args__ = {
        'polymorphic_identity':'device',
        'polymorphic_on':type
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def install_app(remove_old=True):
        pass