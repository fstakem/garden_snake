# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from .base_model import BaseModel
from ...database import sql_db as db


class InstalledApp(BaseModel):
    
    # Properties
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('app.id'), primary_key=True)
    install_time = db.Column(db.DateTime, default=datetime.now)
    uninstall_time = db.Column(db.DateTime, default=datetime.now)
    running = db.Column(db.Boolean)

    # Relationships
    device = db.relationship("Device", back_populates="apps")
    app = db.relationship("App", back_populates="devices")

    __tablename__ = 'installed_app'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def new_app_version(new_version):
    pass