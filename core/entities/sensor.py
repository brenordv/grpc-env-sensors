# -*- coding: utf-8 -*-
from typing import Union
import persistent

from core import validators


class Sensor(persistent.Persistent):
    def __init__(self,
                 sensor_id: str,
                 location_id: str,
                 sensor_name: str):
        self._id: Union[str, None] = None
        self._location_id: Union[str, None] = None
        self._sensor_name: Union[str, None] = None

        self.id = sensor_id
        self.location_id = location_id
        self.sensor_name = sensor_name

    def __str__(self):
        return f"Id: '{self.id}' | Location Id: '{self.location_id}' | Name: '{self.sensor_name}'"

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        validators.is_str_not_null_or_empty(value, "sensor id")

        self._id = value

    @property
    def location_id(self) -> str:
        return self._location_id

    @location_id.setter
    def location_id(self, value: str) -> None:
        validators.is_str_not_null_or_empty(value, "location id")

        self._location_id = value

    @property
    def sensor_name(self) -> str:
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, value: str) -> None:
        validators.is_str_not_null_or_empty(value, "sensor name")

        self._sensor_name = value
