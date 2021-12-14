# -*- coding: utf-8 -*-
from typing import Union
import persistent

from core import validators


class Location(persistent.Persistent):
    def __init__(self,
                 location_id: str,
                 location_name: str):
        self._id: Union[str, None] = None
        self._location_name: Union[str, None] = None

        self.id = location_id
        self.name = location_name

    def __str__(self):
        return f"Id: '{self.id}' | Name: '{self.name}'"

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        validators.is_str_not_null_or_empty(value, "location id")

        self._id = value

    @property
    def name(self) -> str:
        return self._location_name

    @name.setter
    def name(self, value: str) -> None:
        validators.is_str_not_null_or_empty(value, "location name")

        self._location_name = value
