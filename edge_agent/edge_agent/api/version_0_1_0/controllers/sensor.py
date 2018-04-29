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

from edge_agent.db.models.sensor import Sensor as SensorModel


class Sensor(Resource):

    def get(self, id):
        sensor = SensorModel.query.filter_by(id=id).first()

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


class SensorList(Resource):

    def get(self):
        sensors = SensorModel.query.order_by(SensorModel.connection_time).all()
        sensors = [x.to_dict() for x in sensors]

        return jsonify(sensors=sensors)
