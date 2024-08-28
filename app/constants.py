from os import path


_ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))

ENV_FILE = path.join(_ROOT_FOLDER, '.env')

_APP_FOLDER = path.join(_ROOT_FOLDER, 'app')

MODULES_FOLDER = path.join(_APP_FOLDER, 'modules')
MODULE_FOLDER = path.join(MODULES_FOLDER, '{}')
MODULE_IMPORT = 'app.modules.{}'

STATIC_FOLDER = path.join(_APP_FOLDER, 'static')

_STORAGE_FOLDER = path.join(_ROOT_FOLDER, 'storage')
_DATA_FOLDER = path.join(_STORAGE_FOLDER, 'data')
SETUP_FILE = path.join(_DATA_FOLDER, 'setup.json')
DATABASE_FILE = path.join(_DATA_FOLDER, 'database.sqlite3')
