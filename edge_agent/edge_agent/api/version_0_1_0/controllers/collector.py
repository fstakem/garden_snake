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


class Collector(Resource):

    def get(self, id):
        collector = CollectorModel.query.filter_by(id=id).first()

        if collector:
            collector = collector.to_dict()

        return jsonify(collector=collector)

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class CollectorList(Resource):

    def get(self):
        collectors = CollectorModel.query.order_by(CollectorModel.name).all()
        collectors = [x.to_dict() for x in collectors]

        return jsonify(collectors=collectors)