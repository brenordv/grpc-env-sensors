# -*- coding: utf-8 -*-
from datetime import datetime
import dateutil.parser

from core.settings import POST_REQUEST_KEYS


def iso8601_str_to_datetime(str_dt: str) -> datetime:
    return dateutil.parser.isoparse(str_dt) if str_dt is not None and str_dt.strip() not in ("", "-") else None


def merge_dicts(a: dict, b: dict) -> dict:
    for key, item in a.items():
        if isinstance(item, dict):
            a[key] = merge_dicts(item, b.get(key, {}))
        else:
            val = b.get(key)
            if val is None:
                continue
            a[key] = item

    return a


def sanitize_post_save_reading(body):
    sanitized = {}
    for key in POST_REQUEST_KEYS:
        sanitized[key] = body[key]

    return sanitized
