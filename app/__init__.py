from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

_cache = {}


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)

    from .views.main import main_bp
    app.register_blueprint(main_bp)

    from .views.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    _cache['app'] = app
    return app


def get_app():
    return _cache['app']
