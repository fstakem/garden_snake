# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    9.6.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class Link(Resource):

    def get(self, id):
        return 'link get {}'.format(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class LinkList(Resource):

    def get(self):
        return 'link get all'

    def post(self):
        pass
