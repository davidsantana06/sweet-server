from os import environ
from . import path


SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.DATABASE_FILE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(' ')

JSON_SORT_KEYS = False
