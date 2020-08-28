import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = 'a rAndOm StRiNg'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir, 'dev-data.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir, 'data.sqlite')


configs = {
    'Development': DevelopmentConfig,
    'Production': ProductionConfig,

    'default': DevelopmentConfig
}
