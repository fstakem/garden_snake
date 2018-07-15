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
from flask_restful import Api, Resource, url_for
from jinja2 import TemplateNotFound

from edge_agent.database import sql_db
from edge_agent.db.models.sample import Sample
from edge_agent.api.version_0_1_0.controllers.app import App as AppController
from edge_agent.api.version_0_1_0.controllers.app import AppList as AppListController
from edge_agent.api.version_0_1_0.controllers.cloud_source import CloudSource as CloudSourceController
from edge_agent.api.version_0_1_0.controllers.cloud_source import CloudSourceList as CloudSourceListController
from edge_agent.api.version_0_1_0.controllers.cloud_var import CloudVar as CloudVarController
from edge_agent.api.version_0_1_0.controllers.cloud_var import CloudVarList as CloudVarListController
from edge_agent.api.version_0_1_0.controllers.gateway import Gateway as GatewayController
from edge_agent.api.version_0_1_0.controllers.gateway import GatewayList as GatewayListController
from edge_agent.api.version_0_1_0.controllers.installed_app import InstalledApp as InstalledAppController
from edge_agent.api.version_0_1_0.controllers.installed_app import InstalledAppList as InstalledAppListController
from edge_agent.api.version_0_1_0.controllers.link import Link as LinkController
from edge_agent.api.version_0_1_0.controllers.link import LinkList as LinkListController
from edge_agent.api.version_0_1_0.controllers.sample import Sample as SampleController
from edge_agent.api.version_0_1_0.controllers.sample import SampleList as SampleListController
from edge_agent.api.version_0_1_0.controllers.sensor import Sensor as SensorController
from edge_agent.api.version_0_1_0.controllers.sensor import SensorList as SensorListController
from edge_agent.api.version_0_1_0.controllers.sensor_board import SensorBoard as SensorBoardController
from edge_agent.api.version_0_1_0.controllers.sensor_board import SensorBoardList as SensorBoardListController
from edge_agent.api.version_0_1_0.controllers.sensor_model import SensorModel as SensorModelController
from edge_agent.api.version_0_1_0.controllers.sensor_model import SensorModelList as SensorModelListController

dir_path = os.path.dirname(os.path.realpath(__file__))

version_value = '0_1_0'
version_name = 'v' + version_value

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
rest_api.add_resource(AppController, '/app/<int:id>')
rest_api.add_resource(AppListController, '/app/all')
rest_api.add_resource(CloudSourceController, '/cloud_source/<int:id>')
rest_api.add_resource(CloudSourceListController, '/cloud_source/all')
rest_api.add_resource(CloudVarController, '/cloud_var/<int:id>')
rest_api.add_resource(CloudVarListController, '/cloud_var/all')
rest_api.add_resource(GatewayController, '/gateway/<int:id>')
rest_api.add_resource(GatewayListController, '/gateway/all')
rest_api.add_resource(InstalledAppController, '/installed_app/<int:id>')
rest_api.add_resource(InstalledAppListController, '/installed_app/all')
rest_api.add_resource(LinkController, '/link/<int:id>')
rest_api.add_resource(LinkListController, '/link/all')
rest_api.add_resource(SampleController, '/sample/<int:id>')
rest_api.add_resource(SampleListController, '/sample/all')
rest_api.add_resource(SensorController, '/sensor/<int:id>')
rest_api.add_resource(SensorListController, '/sensor/all')
rest_api.add_resource(SensorBoardController, '/sensor_board/<int:id>')
rest_api.add_resource(SensorBoardListController, '/sensor_board/all')
rest_api.add_resource(SensorModelController, '/sensor_model/<int:id>')
rest_api.add_resource(SensorModelListController, '/sensor_model/all')

rest_api.init_app(app_v0_1_0)

