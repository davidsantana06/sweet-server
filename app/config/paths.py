from os import path


ROOT_DIR = path.abspath(path.join(path.dirname(__file__), '..', '..'))
''' / '''

ENV_FILE = path.join(ROOT_DIR, '.env')
''' /.env '''

PARAMETERS_FILE = path.join(ROOT_DIR, 'app', 'config', 'parameters.py')
''' /app/config/parameters.py '''

STORAGE_DIR = path.join(ROOT_DIR, 'storage')
''' /storage/ '''

SETUP_FILE = path.join(STORAGE_DIR, 'setup.json')
''' /storage/setup.json '''

DATABASE_FILE = path.join(STORAGE_DIR, 'database.sqlite3')
''' /storage/database.sqlite3 '''
