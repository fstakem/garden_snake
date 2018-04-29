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

from edge_agent.db.models.gateway import Gateway as GatewayModel
from edge_agent.db.schema.gateway_schema import GatewaySchema


class Gateway(Resource):
    schema = GatewaySchema()

    def get(self, id):
        gateway = GatewayModel.query.filter_by(id=id).first()

        if gateway:
            gateway = self.schema.dump(x).data

        return jsonify(gateway=gateway)

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class GatewayList(Resource):
    schema = GatewaySchema()

    def get(self):
        gateways = GatewayModel.query.order_by(GatewayModel.name).all()
        gateways = [self.schema.dump(x).data for x in gateways]

        return jsonify(gateways=gateways)
