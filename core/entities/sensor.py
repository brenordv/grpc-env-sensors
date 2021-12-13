# -*- coding: utf-8 -*-
from typing import Union
import persistent


class Sensor(persistent.Persistent):
    def __init__(self,
                 sensor_id: str,
                 location_id: str,
                 sensor_name: str):
        self.__id__: Union[str, None] = None
        self.__location_id__: Union[str, None] = None
        self.__sensor_name__: Union[str, None] = None

        self.id = sensor_id
        self.location_id = location_id
        self.sensor_name = sensor_name

    def __str__(self):
        return f"Id: '{self.id}' | Location Id: '{self.location_id}' | Name: '{self.sensor_name}'"

    @property
    def id(self) -> str:
        return self.__id__

    @id.setter
    def id(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Sensor Id cannot be null")

        self.__id__ = value

    @property
    def location_id(self) -> str:
        return self.__location_id__

    @location_id.setter
    def location_id(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Location Id cannot be null")

        self.__location_id__ = value

    @property
    def sensor_name(self) -> str:
        return self.__sensor_name__

    @sensor_name.setter
    def sensor_name(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Sensor Name cannot be null")

        self.__sensor_name__ = value
