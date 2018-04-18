# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.11.18   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import json
from os.path import dirname, abspath


def load_config():
    env = os.environ['ENV'].lower()
    config_dir_path = dirname(abspath(__file__))
    config_file = env + '.json'
    config_path = os.path.join(config_dir_path, config_file)
    assert os.path.isfile(config_path)

    with open(config_path) as config_data:    
        config = json.load(config_data)

    # ======== Transform the config file
    config['env'] = env

    project_path = dirname(dirname(dirname(abspath(__file__))))
    config['project_path'] = project_path
    config['app_path'] = os.path.join(project_path, config['app_name'])

    db_path = os.path.join(config['app_path'], 'db', 'data', config['db_name'])
    config['db_path'] = db_path
    db_connect_str = 'sqlite:///{}'.format(db_path)
    config['db_connect_str'] = db_connect_str

    return config


