# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization

from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_message = "Bu sayfaya erişmek için giriş yapmalısınız"
    login_manager.login_view = "auth.login"

    return app