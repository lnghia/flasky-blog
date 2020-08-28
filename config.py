import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = 'a rAndOm StRiNg'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SSL_DISABLE = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir, 'dev-data.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        pass


class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

        # handle proxy server headers
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)


configs = {
    'Development': DevelopmentConfig,
    'Production': ProductionConfig,
    'Heroku': HerokuConfig,

    'default': DevelopmentConfig
}
