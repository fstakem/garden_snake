# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.11.18  
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os

from flask import Blueprint, render_template, abort, request, redirect, session
from flask import current_app
from flask_restful import Api, Resource, url_for
from jinja2 import TemplateNotFound

from edge_agent.database import sql_db
from edge_agent.db.models.sample import Sample

dir_path = os.path.dirname(os.path.realpath(__file__))

version_value = '0_1_0'
version_name = 'app_v' + version_value

app_v0_1_0 = Blueprint(version_name, version_name, 
    static_folder='edge_agent/api/version_0_1_0/static', 
    static_url_path='',
    template_folder='edge_agent/api/version_0_1_0/templates')


# Web routes
@app_v0_1_0.route('/')
def version_hello():
    return 'v{}'.format(version_value)

@app_v0_1_0.route('/index')
def index():
    return render_template('index.html')

@app_v0_1_0.route('/db_test')
def db_test():
    sample = Sample()
    return 'OK'


# Basic restful routes
rest_api = Api(app_v0_1_0)


