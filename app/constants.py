from os import path


ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))

ENV_FILE = path.join(ROOT_FOLDER, '.env')

APP_FOLDER = path.join(ROOT_FOLDER, 'app')

MODULES_FOLDER = path.join(APP_FOLDER, 'modules')
MODULE_FOLDER = path.join(MODULES_FOLDER, '{}')
MODULE_IMPORT = 'app.modules.{}'

STATIC_FOLDER = path.join(APP_FOLDER, 'static')

STORAGE_FOLDER = path.join(ROOT_FOLDER, 'storage')
DATA_FOLDER = path.join(STORAGE_FOLDER, 'data')
SETUP_FILE = path.join(DATA_FOLDER, 'setup.json')
DATABASE_FILE = path.join(DATA_FOLDER, 'database.sqlite3')
