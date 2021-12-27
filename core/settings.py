# -*- coding: utf-8 -*-
import json
import logging
from pathlib import Path
from os import makedirs
import copy

POST_REQUEST_KEYS = ["sensor_id", "reading_location_id", "reading_value", "read_at"]
ROOT_APP_PATH = Path(__file__).parent.parent
SETTINGS_FILE = ROOT_APP_PATH.joinpath("settings.json")
APP_DATA_FOLDER = ROOT_APP_PATH.joinpath(".app")
DB_FILE = APP_DATA_FOLDER.joinpath("database.db")
SECRETS_FILE = ROOT_APP_PATH.joinpath("secrets.env.json")
DEFAULT_SETTINGS = {
    "logging": {
        "level": "DEBUG"
    },
    "api": {
        "host": "0.0.0.0",
        "port": 14200
    }
}

# NOTE: Don't do this. This is bad, very bad! Use a key-vault of some kind... anything but this type of thing!
# This is just a test application running locally, so it's almost ok.
DEFAULT_SECRETS = {
    "connection_strings": {
        "mongodb_primary": "mongodb://root:root123@localhost:27017"
    }
}

if not APP_DATA_FOLDER.exists():
    makedirs(APP_DATA_FOLDER)

try:
    SETTINGS = json.loads(json.dumps(DEFAULT_SETTINGS))
except (TypeError, ValueError):
    SETTINGS = copy.deepcopy(DEFAULT_SETTINGS)


try:
    SECRETS = json.loads(json.dumps(DEFAULT_SECRETS))
except (TypeError, ValueError):
    SECRETS = copy.deepcopy(DEFAULT_SECRETS)


if SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
        SETTINGS = SETTINGS | json.load(file)

# Just a reminder: Do not do this! Ever!
if SECRETS_FILE.exists():
    with open(SECRETS_FILE, "r", encoding="utf-8") as file:
        SECRETS = SECRETS | json.load(file)


def configure_application_logging():
    logging.basicConfig(**SETTINGS.get("logging", {}))
