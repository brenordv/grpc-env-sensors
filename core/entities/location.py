# -*- coding: utf-8 -*-
from typing import Union
import persistent


class Location(persistent.Persistent):
    def __init__(self,
                 location_id: str,
                 location_name: str):
        self.__id__: Union[str, None] = None
        self.__location_name__: Union[str, None] = None

        self.id = location_id
        self.name = location_name

    def __str__(self):
        return f"Id: '{self.id}' | Name: '{self.name}'"

    @property
    def id(self) -> str:
        return self.__id__

    @id.setter
    def id(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Location Id cannot be null")

        self.__id__ = value

    @property
    def name(self) -> str:
        return self.__location_name__

    @name.setter
    def name(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Location Name cannot be null")

        self.__location_name__ = value
