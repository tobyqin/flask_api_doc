from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

_cache = {}


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    from .views.main import main
    app.register_blueprint(main)

    from .views.api import api
    app.register_blueprint(api, url_prefix='/api')

    _cache['app'] = app
    return app


def get_app():
    return _cache['app']
