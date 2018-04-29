# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.29.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.database import marsh
from edge_agent.db.models.sensor import Sensor


class SensorSchema(marsh.ModelSchema):
    class Meta:
        model = Sensor