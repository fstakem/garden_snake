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
from edge_agent.db.schema.sensor_model_schema import SensorModelSchema


class SensorModel(Resource):
    schema = SensorModelSchema()

    def get(self, id):
        sensor = SensorModelDb.query.filter_by(id=id).first()

        if sensor:
            sensor = self.schema.dump(x).data

        return jsonify(sensor=sensor)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SensorModelList(Resource):
    schema = SensorModelSchema()

    def get(self):
        sensors = SensorModelDb.query.order_by(SensorModelDb.name).all()
        sensors = [self.schema.dump(x).data for x in sensors]

        return jsonify(sensors=sensors)

    def post(self):
        pass
