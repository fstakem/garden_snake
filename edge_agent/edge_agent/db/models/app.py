# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.21.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from .base_model import BaseModel
from ...database import sql_db as db


class App(BaseModel):
    
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String)
    version = db.Column(db.String)
    latest_version = db.Column(db.Boolean)

    # Relationships
    installed_apps = db.relationship("InstalledApp", back_populates="app")

    __tablename__ = 'app'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def new_app_version(new_version):
        pass