# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.29.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from edge_agent.app import marsh
from edge_agent.db.models.installed_app import InstalledApp


class InstalledAppSchema(marsh.ModelSchema):
    class Meta:
        model = InstalledApp