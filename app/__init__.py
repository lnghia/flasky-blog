from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from config import configs
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
moment = Moment()
bootstrap = Bootstrap()


def create_app(config='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config])
    configs[config].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    # redirect any requests sent to http:// to https://
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    # attach blueprints here
    from .main import main as MainBlueprint
    app.register_blueprint(MainBlueprint)

    from .auth import auth as AuthenticationBlueprint
    app.register_blueprint(AuthenticationBlueprint, url_prefix='/auth')

    return app
