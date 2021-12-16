# -*- coding: utf-8 -*-
import json
import logging
from pathlib import Path
from os import makedirs
import copy

ROOT_APP_PATH = Path(__file__).parent.parent
SETTINGS_FILE = ROOT_APP_PATH.joinpath("settings.json")
APP_DATA_FOLDER = ROOT_APP_PATH.joinpath(".app")
DB_FILE = APP_DATA_FOLDER.joinpath("database.db")
DEFAULT_SETTINGS = {
  "logging": {
    "level": "DEBUG"
  },
  "api": {
    "host": "0.0.0.0",
    "port": 14200
  }
}

if not APP_DATA_FOLDER.exists():
    makedirs(APP_DATA_FOLDER)

try:
    SETTINGS = json.loads(json.dumps(DEFAULT_SETTINGS))
except:
    SETTINGS = copy.deepcopy(DEFAULT_SETTINGS)

if SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
        SETTINGS = SETTINGS | json.load(file)


def configure_application_logging():
    logging.basicConfig(**SETTINGS.get("logging", {}))
