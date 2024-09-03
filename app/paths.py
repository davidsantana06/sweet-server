from os import path


_ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
ENV_FILE = path.join(_ROOT_FOLDER, '.env')

_STORAGE_FOLDER = path.join(_ROOT_FOLDER, 'storage')

_DATA_FOLDER = path.join(_STORAGE_FOLDER, 'data')
SETUP_FILE = path.join(_DATA_FOLDER, 'setup.json')
DATABASE_FILE = path.join(_DATA_FOLDER, 'database.sqlite3')
