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

from edge_agent.db.models.sample import Sample as SampleModel


class Sample(Resource):

    def get(self, id):
        sample = SampleModel.query.filter_by(id=id).first()

        if sample:
            sample = sample.to_dict()

        return jsonify(sample=sample)

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SampleList(Resource):

    def get(self):
        samples = SampleModel.query.order_by(SampleModel.id).all()
        samples = [x.to_dict() for x in samples]

        return jsonify(samples=samples)
