from pathlib import Path


ROOT_DIR = Path.cwd()
''' / '''

ENV_FILE = ROOT_DIR / '.env'
''' /.env '''

STORAGE_DIR = ROOT_DIR / 'storage'
''' /storage/ '''

DATABASE_FILE = STORAGE_DIR / 'database.sqlite3'
''' /storage/database.sqlite3 '''

SETUP_DIR = STORAGE_DIR / 'setup'
''' /storage/setup/ '''

DEFAULT_CATEGORIES_DATA_FILE = SETUP_DIR / 'default_categories.json'
'''  /storage/setup/default_categories.json '''

DEFAULT_COLLABORATOR_DATA_FILE = SETUP_DIR / 'default_collaborator.json'
'''  /storage/setup/default_collaborator.json '''

DEFAULT_PAYMENT_METHODS_DATA_FILE = SETUP_DIR / 'default_payment_methods.json'
'''  /storage/setup/default_payment_methods.json '''

USER_DATA_FILE = SETUP_DIR / 'user.json'
'''  /storage/setup/user.json '''
