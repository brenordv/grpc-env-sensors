# -*- coding: utf-8 -*-
from flask import Flask

from api.blueprints.sensor_blueprint import sensors_controller

app = Flask(__name__)
app.register_blueprint(sensors_controller)


@app.route("/", methods=["GET", ])
def api_home():
    return "Hello world... to the grpc_env_sensors api!"
