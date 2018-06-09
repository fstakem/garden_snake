# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.6.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class SensorBoard(Resource):

    def get(self, id):
        return 'sensor board get {}'.format(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SensorBoardList(Resource):

    def get(self):
        return 'sensor board get all'

    def post(self):
        pass
