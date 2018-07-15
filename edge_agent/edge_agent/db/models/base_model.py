# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.11.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime

from sqlalchemy.orm import object_mapper

from edge_agent.database import sql_db as db


class BaseModel(db.Model):
    
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    __abstract__ = True

    def __int__(**kwargs):
        super.__init__(**kwargs)

