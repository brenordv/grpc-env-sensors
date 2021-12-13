# -*- coding: utf-8 -*-
from os import environ

from core.utils import load_secrets_from_file


def load_environment_vars():
    required_keys = ["telegram_bot_key", "telegram_default_chat_id"]
    env_vars = {}

    for key in required_keys:
        env_vars[key] = environ.get(key)

    if not any(v is None for v in env_vars.values()):
        return env_vars

    file_vars = load_secrets_from_file()
    for key, value in env_vars.items():
        if value is not None:
            continue

        env_vars[key] = file_vars.get(key)

    missing_values = [key for key in env_vars.keys() if env_vars[key] is None]
    if len(missing_values) > 0:
        raise ValueError(f"The following required secrets are missing: {', '.join(missing_values)}")

    return env_vars


ENV_VARS = load_environment_vars()
