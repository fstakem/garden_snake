# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.6.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class CloudSource(Resource):

    def get(self, id):
        return 'cloud source get {}'.format(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class CloudSourceList(Resource):

    def get(self):
        return 'cloud source get all'

    def post(self):
        pass
