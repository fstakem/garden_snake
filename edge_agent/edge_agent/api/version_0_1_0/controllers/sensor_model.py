# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.28.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource
from flask import jsonify

from edge_agent.db.models.sensor_model import SensorModel as SensorModelDb


class SensorModel(Resource):

    def get(self, id):
        sensor = SensorModelDb.query.filter_by(id=id).first()

        if sensor:
            sensor = sensor.to_dict()

        return jsonify(sensor=sensor)

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SensorModelList(Resource):

    def get(self):
        sensors = SensorModelDb.query.order_by(SensorModelDb.name).all()
        sensors = [x.to_dict() for x in sensors]

        return jsonify(sensors=sensors)
