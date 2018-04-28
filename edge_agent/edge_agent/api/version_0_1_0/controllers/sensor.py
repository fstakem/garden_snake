# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.28.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class Sensor(Resource):

    def get(self, id):
        return 'sensor get {}'.format(id)

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SensorList(Resource):

    def get(self):
        return 'sensor get all'
