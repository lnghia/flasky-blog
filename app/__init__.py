from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from config import configs

db = SQLAlchemy()


def create_app(config='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config])
    db.init_app(app)

    # attach blueprints here
    from .main import main as MainBlueprint
    app.register_blueprint(MainBlueprint)

    return app
