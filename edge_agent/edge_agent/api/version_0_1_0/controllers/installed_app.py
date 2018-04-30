# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.28.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class InstalledApp(Resource):

    def get(self, id):
        return 'installed app get {}'.format(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class InstalledAppList(Resource):

    def get(self):
        return 'installed app get all'

    def post(self):
        pass
