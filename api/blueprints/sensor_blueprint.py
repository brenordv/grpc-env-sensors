# -*- coding: utf-8 -*-
import json

from flask import Blueprint, jsonify, make_response

from client.sensor_client import SensorClient
from core import validators

sensors_controller = Blueprint("sensors", __name__, url_prefix="/sensors/v1")


@sensors_controller.route("/", methods=["GET", ])
def get_sensor_readings():
    client = SensorClient()
    result = client.get_readings()
    return jsonify({
        **result,
        "payload": [p.__dict__ for p in result["payload"]]
    })


@sensors_controller.route("/<reading_id>", methods=["GET", ])
def get_sensor_reading(reading_id: str):
    try:
        label = "reading_id"
        validators.is_str_not_null_or_empty(reading_id, label)
        validators.is_valid_guid(reading_id, label)
    except ValueError as ve:
        return str(ve), 400

    client = SensorClient()
    result = client.get_reading(reading_id)

    if not result["success"]:
        return result["error_message"], 400

    if result["payload"] is None:
        return result["error_message"], 404

    return jsonify({
        **result,
        "payload": result["payload"].__dict__ if result["payload"] is not None else None
    })
