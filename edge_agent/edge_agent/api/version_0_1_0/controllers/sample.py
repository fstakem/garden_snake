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
from edge_agent.db.schema.sample_schema import SampleSchema


class Sample(Resource):
    schema = SampleSchema()

    def get(self, id):
        sample = SampleModel.query.filter_by(id=id).first()

        if sample:
            sample = self.schema.dump(x).data

        return jsonify(sample=sample)

    def put(self, id):
        pass

    def post(self, id):
        data = {}
        sample = SampleModel(data=data)

    def delete(self, id):
        pass

    def update(self, id):
        pass


class SampleList(Resource):
    schema = SampleSchema()

    def get(self):
        samples = SampleModel.query.order_by(SampleModel.id).all()
        samples = [self.schema.dump(x).data for x in samples]

        return jsonify(samples=samples)
