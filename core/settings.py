# -*- coding: utf-8 -*-
from pathlib import Path
from os import makedirs

APP_DATA_FOLDER = Path(__file__).parent.parent.joinpath(".app")
DB_FILE = APP_DATA_FOLDER.joinpath("database.db")


if not APP_DATA_FOLDER.exists():
    makedirs(APP_DATA_FOLDER)
