# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.12.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.app import marsh
from edge_agent.db.models.measurement import Measurement


class MeasurementSchema(marsh.ModelSchema):
    class Meta:
        model = Measurement