from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from config import configs

db = SQLAlchemy()


def create_app(config='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config])
    configs[config].init_app(app)
    db.init_app(app)

    # redirect any requests sent to http:// to https://
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    # attach blueprints here
    from .main import main as MainBlueprint
    app.register_blueprint(MainBlueprint)

    return app
