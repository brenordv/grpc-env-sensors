# -*- coding: utf-8 -*-
from api.api import app
from core.settings import SETTINGS


def main():
    app.run(**SETTINGS["api"], )


if __name__ == '__main__':
    main()
