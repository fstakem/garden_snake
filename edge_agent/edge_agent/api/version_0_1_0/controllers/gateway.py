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


class Gateway(Resource):

    def get(self, id):
        gateway = GatewayModel.query.filter_by(id=id).first()

        if gateway:
            gateway = gateway.to_dict()

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

    def get(self):
        gateways = GatewayModel.query.order_by(GatewayModel.name).all()
        gateways = [x.to_dict() for x in gateways]

        return jsonify(gateways=gateways)
