from flask import Flask
from flask_cors import CORS

from nst_path_api.path_blueprint import path_blueprint


def create_app(config_object="nst_path_api.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register Flask extensions."""
    app.register_blueprint(path_blueprint)
    return