# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.app import marsh
from edge_agent.db.models.cloud_source import CloudSource


class CloudSourceSchema(marsh.ModelSchema):
    class Meta:
        model = CloudSource