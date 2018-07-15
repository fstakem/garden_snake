# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.6.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class CloudVar(Resource):

    def get(self, id):
        return 'cloud var get {}'.format(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class CloudVarList(Resource):

    def get(self):
        return 'cloud var get all'

    def post(self):
        pass
