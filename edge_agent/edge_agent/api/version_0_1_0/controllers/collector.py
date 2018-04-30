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

from edge_agent.db.models.collector import Collector as CollectorModel
from edge_agent.db.schema.collector_schema import CollectorSchema


class Collector(Resource):
    schema = CollectorSchema()

    def get(self, id):
        collector = CollectorModel.query.filter_by(id=id).first()

        if collector:
            collector = self.schema.dump(collector).data

        return jsonify(collector=collector)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class CollectorList(Resource):
    schema = CollectorSchema()

    def get(self):
        collectors = CollectorModel.query.order_by(CollectorModel.name).all()
        collectors = [self.schema.dump(x).data for x in collectors]

        return jsonify(collectors=collectors)

    def post(self):
        pass