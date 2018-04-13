# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    8.11.16   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask import Blueprint
from flask_restful import Api, Resource, url_for

version = 'v0_1_0'
blueprint_name = 'api_{}'.format(version)
app_v0_1_0 = Blueprint(blueprint_name, __name__)

@app_v1_0_0.route('/hello')
def version_hello():
    return 'Hello {}'.format(version)


# Restful
rest_api = Api(app_v1_0_0)

class RestfulHellos(Resource):

    def get(self):
        return 'Restful hello yall'


class RestfulHello(Resource):

    def get(self, id):
        return 'Restful hello {}'.format(id)

rest_api.add_resource(RestfulHellos, '/restful_hello')
rest_api.add_resource(RestfulHello, '/restful_hello/<int:id>')