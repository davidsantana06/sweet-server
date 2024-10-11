from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


cors = CORS()
database = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
