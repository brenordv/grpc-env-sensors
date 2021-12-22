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


def is_number(value: Union[str, int, float, None], label: str) -> None:
    if isinstance(value, (int, float)):
        return

    is_str_not_null_or_empty(value, label)
    try:
        int(value)
        return
    except ValueError:
        pass

    try:
        float(value)
        return
    except ValueError:
        pass

    raise ValueError(f"{label} with value '{value}' is not a number")


def is_of_type(value, value_type: Union[Type[any], Tuple[Type[any]]], label: str) -> None:
    if isinstance(value, value_type):
        return

    if isinstance(value_type, (tuple, list)):
        expected_types = ', '.join(value_type)
        raise TypeError(f"{label} must be one of the following types '{expected_types}'. got '{type(value).__name__}'")

    expected_types = value_type.__name__
    raise TypeError(f"{label} must be of type '{expected_types}'. got '{type(value).__name__}'")


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
