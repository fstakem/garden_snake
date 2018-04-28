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

from edge_agent.api.version_0_1_0.controllers.app import App as AppController
from edge_agent.api.version_0_1_0.controllers.app import AppList as AppListController
from edge_agent.api.version_0_1_0.controllers.collector import Collector as CollectorController
from edge_agent.api.version_0_1_0.controllers.collector import CollectorList as CollectorListController
from edge_agent.api.version_0_1_0.controllers.gateway import Gateway as GatwayController
from edge_agent.api.version_0_1_0.controllers.gateway import GatewayList as GatewayListController
from edge_agent.api.version_0_1_0.controllers.installed_app import InstalledApp as InstalledAppController
from edge_agent.api.version_0_1_0.controllers.installed_app import InstalledAppList as InstalledAppListController
from edge_agent.api.version_0_1_0.controllers.sample import Sample as SampleController
from edge_agent.api.version_0_1_0.controllers.sample import SampleList as SampleListController
from edge_agent.api.version_0_1_0.controllers.sensor import Sensor as SensorController
from edge_agent.api.version_0_1_0.controllers.sensor import SensorList as SensorListController
from edge_agent.api.version_0_1_0.controllers.sensor_model import SensorModel as SensorModelController
from edge_agent.api.version_0_1_0.controllers.sensor_model import SensorModelList as SensorModelListController

dir_path = os.path.dirname(os.path.realpath(__file__))

version_value = '0_1_0'
version_name = 'app_v' + version_value

app_v0_1_0 = Blueprint(version_name, version_name, 
    static_folder='edge_agent/api/version_0_1_0/static', 
    static_url_path='/test',
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
rest_api.resource(AppController, '/app/<int:id>')
rest_api.resource(AppListController, '/app/all')
rest_api.resource(CollectorController, '/collector/<int:id>')
rest_api.resource(CollectorListController, '/collector/all')
rest_api.resource(GatewayController, '/gateway/<int:id>')
rest_api.resource(GatewayListController, '/gateway/all')
rest_api.resource(InstalledAppController, '/installed_app/<int:id>')
rest_api.resource(InstalledAppListController, '/installed_app/all')
rest_api.resource(SampleController, '/sample/<int:id>')
rest_api.resource(SampleListController, '/sample/all')
rest_api.resource(SensorController, '/sensor/<int:id>')
rest_api.resource(SensorListController, '/sensor/all')
rest_api.resource(SensorModelController, '/sensor_model/<int:id>')
rest_api.resource(SensorModelListController, '/sensor_model/all')


