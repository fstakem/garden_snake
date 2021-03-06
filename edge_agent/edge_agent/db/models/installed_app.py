# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from edge_agent.db.models.base_model import BaseModel
from edge_agent.db.models.serializer import Serializer
from edge_agent.database import sql_db as db


class InstalledApp(BaseModel, Serializer):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    app_id = db.Column(db.Integer, db.ForeignKey('app.id'))
    install_time = db.Column(db.DateTime, default=datetime.now)
    uninstall_time = db.Column(db.DateTime, default=datetime.now)
    running = db.Column(db.Boolean)

    # Relationships
    device = db.relationship("Device", back_populates="installed_apps")
    app = db.relationship("App", back_populates="installed_apps")

    __tablename__ = 'installed_app'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def new_app_version(new_version):
    pass