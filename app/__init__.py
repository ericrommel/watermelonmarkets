import os
from pathlib import Path

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import app_config
from log import Log

LOGGER = Log("watermelonmarket").get_logger(logger_name="app")

db = SQLAlchemy()

current_dir = os.path.abspath(os.path.dirname(__file__))


def create_app(config_name):
    """
    This is the application factory function. It creates and configures the app
    """

    LOGGER.info(f"Initialize Flask app: {__name__}")
    app = Flask(__name__, instance_relative_config=True)

    csrf = CSRFProtect(app)

    LOGGER.info("Create 'db' folder if it is not done yet")
    try:
        os.makedirs(Path(current_dir, "db"))
        LOGGER.info("'db' folder created")
    except OSError:
        pass

    db_dir = Path(current_dir, "db")

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py", silent=True)
    app.config.from_mapping(
        SECRET_KEY="TeMpOrArYkEyHaSbEeNuSeD",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,  # avoid FSADeprecationWarning
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(db_dir, 'watermelonmarket.db')}",
    )

    LOGGER.info("Initialize the application to use with its setup DB")
    Bootstrap(app)
    db.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)

    from app.home import home as home_bprint

    app.register_blueprint(home_bprint)

    return app
