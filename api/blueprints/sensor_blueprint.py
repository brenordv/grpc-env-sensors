# -*- coding: utf-8 -*-
import json

from flask import Blueprint, jsonify, make_response, request
from raccoon_simple_stopwatch.stopwatch import StopWatch

from client.sensor_client import SensorClient
from core import validators
from core.converters import From, KnownTypes
from core.settings import POST_REQUEST_KEYS
from core.utils import sanitize_post_save_reading

sensors_controller = Blueprint("sensors", __name__, url_prefix="/sensors/v1")


@sensors_controller.route("/", methods=["GET", ])
def get_sensor_readings():
    limit = request.args.get("limit")
    if limit is not None:
        validators.is_number(limit, "limit result")
        limit = From(limit).to(KnownTypes.INT)

    result = SensorClient().get_readings(limit=limit)
    return jsonify({
        **result,
        "payload": [p.__dict__ for p in result["payload"]]
    })


@sensors_controller.route("/", methods=["POST", ])
def save_sensor_reading():
    if not request.json:
        return "Post has no body. What should I save?", 400

    start = StopWatch(auto_start=True)
    body = request.json
    missing_keys = [k for k in POST_REQUEST_KEYS if k not in body]
    if len(missing_keys) > 0:
        return f"Invalid post. The following keys are missing: {', '.join(missing_keys)}", 400

    try:
        sanitized_body = sanitize_post_save_reading(body)
        print(f"Body sanitization: {start.elapsed()}")
        result = SensorClient().save_new_reading(**sanitized_body)
        print(f"Response from server: {start.elapsed()}")
    except Exception as e:
        print(f"Error: {e} || {body}")
        raise

    response = make_response(json.dumps(result), 201)
    print(f"Response ready to send: {start.end()}")
    return response


@sensors_controller.route("/<reading_id>", methods=["GET", ])
def get_sensor_reading(reading_id: str):
    try:
        label = "reading_id"
        validators.is_str_not_null_or_empty(reading_id, label)
        validators.is_valid_guid(reading_id, label)
    except ValueError as ve:
        return str(ve), 400

    result = SensorClient().get_reading(reading_id)

    if not result["success"]:
        return result["error_message"], 400

    if result["payload"] is None:
        return result["error_message"], 404

    return jsonify({
        **result,
        "payload": result["payload"].__dict__ if result["payload"] is not None else None
    })
