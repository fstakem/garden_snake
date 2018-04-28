# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.11.18  
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import logging

from flask import request, url_for, jsonify, Flask

from edge_agent.database import sql_db
from edge_agent.config.config import load_config
from edge_agent.api.version_0_1_0.controllers.main import app_v0_1_0


# Framework globals
# -----------------------------------------------------
flask_app = None
current_app = app_v0_1_0


# Config
app_config      = load_config()

# Logger
logger          = None
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

# App
flask_app = Flask(__name__)
flask_app.secret_key                                = 'TTS96tKYthZh2V2jO7Bwi1c4BO0BFYfe8YnDegkg'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
flask_app.config['SQLALCHEMY_DATABASE_URI']         = app_config['db_connect_str']
flask_app.register_blueprint(current_app)

# Init DB
sql_db.init_app(flask_app)

# App code
# -----------------------------------------------------
@flask_app.route('/')
def root():
    return 'Root page'

@flask_app.route('/version')
def version():
    return config['version']

@flask_app.route('/routes')
def routes():
    rules = [x for x in flask_app.url_map.iter_rules()]
    routes = {x.rule: '{} {}'.format(x.endpoint, x.methods) for x in rules}

    return jsonify(routes)