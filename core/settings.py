# -*- coding: utf-8 -*-
import json
import logging
from pathlib import Path
from os import makedirs


ROOT_APP_PATH = Path(__file__).parent.parent
SETTINGS_FILE = ROOT_APP_PATH.joinpath("settings.json")
APP_DATA_FOLDER = ROOT_APP_PATH.joinpath(".app")
DB_FILE = APP_DATA_FOLDER.joinpath("database.db")


if not APP_DATA_FOLDER.exists():
    makedirs(APP_DATA_FOLDER)

if SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
        SETTINGS = json.load(file)
else:
    SETTINGS = {
        "logging": {
            "level": "DEBUG"
        }
    }


def configure_application_logging():
    logging.basicConfig(**SETTINGS.get("logging", {}))
