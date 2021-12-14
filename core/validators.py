# -*- coding: utf-8 -*-
from typing import Type, Union, Tuple
from uuid import UUID


def is_not_null(value, label: str) -> None:
    if value is not None:
        return

    raise ValueError(f"{label} cannot be null")


def is_str_not_null_or_empty(value: str, label: str) -> None:
    is_not_null(value, label)
    is_of_type(value, str, label)

    if value.strip() != "":
        return

    raise ValueError(f"{label} cannot be null or empty text")


def is_of_type(value, value_type: Union[Type[any], Tuple[Type[any]]], label: str) -> None:
    if isinstance(value, value_type):
        return

    raise TypeError(f"{label} must be a '{value_type.__name__}'. got '{type(value).__name__}'")


def is_valid_guid(guid: str, label: str) -> None:
    try:
        uuid_obj = UUID(guid, version=4)
        error = str(uuid_obj) != guid
    except ValueError:
        error = True

    if not error:
        return

    raise ValueError(f"{label} must be a valid guid (UUID4)")


def is_number_between(value, min_val: Union[int, float], max_val: Union[int, float], label: str) -> None:
    is_of_type(value, (int, float), label)
    if float(min_val) <= float(value) <= float(max_val):
        return

    raise ValueError(f"{label} must be between {min_val} and {max_val}. Got {value}")
