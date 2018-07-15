# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    6.9.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.app import marsh
from edge_agent.db.models.link import Link


class LinkSchema(marsh.ModelSchema):
    class Meta:
        model = Link