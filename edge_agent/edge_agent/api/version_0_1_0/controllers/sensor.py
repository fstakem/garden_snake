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
from edge_agent.db.schema.sensor_schema import SensorSchema


class Sensor(Resource):
    schema = SensorSchema()

    def get(self, id):
        sensor = SensorModel.query.filter_by(id=id).first()

        if sensor:
            sensor = self.schema.dump(sensor).data

        return jsonify(sensor=sensor)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SensorList(Resource):
    schema = SensorSchema()

    def get(self):
        sensors = SensorModel.query.order_by(SensorModel.connection_time).all()
        sensors = [self.schema.dump(x).data for x in sensors]

        return jsonify(sensors=sensors)

    def post(self):
        pass
