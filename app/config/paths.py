from os import path


ROOT_DIR = path.abspath(path.join(path.dirname(__file__), '..', '..'))
ENV_FILE = path.join(ROOT_DIR, '.env')

PARAMETERS_FILE = path.join(ROOT_DIR, 'app', 'config', 'parameters.py')

STORAGE_DIR = path.join(ROOT_DIR, 'storage')
SETUP_FILE = path.join(STORAGE_DIR, 'setup.json')
DATABASE_FILE = path.join(STORAGE_DIR, 'database.sqlite3')
