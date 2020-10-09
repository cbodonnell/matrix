from flask import Flask
from flask_cors import CORS
from .path_blueprint import path_blueprint


app = Flask(__name__)

# Reads environment variable FLASK_ENV
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print('ENV is set to: %s' % app.config["ENV"])

cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.register_blueprint(path_blueprint)
