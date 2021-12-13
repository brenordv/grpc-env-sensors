# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from typing import Union
import persistent

from core.utils import is_valid_guid


class SensorReading(persistent.Persistent):
    def __init__(self,
                 sensor_id: str,
                 reading_location_id: str,
                 reading_value: float,
                 trusted_reading: bool = False,
                 location_known: bool = False,
                 location_accurate: bool = False,
                 reading_id: Union[str, None] = None,
                 overall_integrity: float = 0.0,
                 is_processed: bool = False,
                 read_at: Union[datetime, None] = None,
                 received_at: Union[datetime, None] = None,
                 updated_at: Union[datetime, None] = None):

        self._id: Union[str, None] = None
        self._sensor_id: Union[str, None] = None
        self._reading_location_id: Union[str, None] = None
        self._reading_value: Union[float, None] = None
        self._is_trusted_reading: bool = trusted_reading
        self._is_location_known: bool = location_known
        self._is_location_accurate: bool = location_accurate
        self._is_processed: bool = is_processed
        self._read_at: Union[datetime, None] = read_at
        self._received_at: Union[datetime, None] = None
        self._updated_at: Union[datetime, None] = updated_at
        self._overall_integrity: float = -1.0

        self.sensor_id = sensor_id
        self.reading_location_id = reading_location_id
        self.reading_value = reading_value
        self.overall_integrity = overall_integrity

        if received_at is not None:
            self.received_at = received_at

        self.id = str(uuid.uuid4()) if reading_id is None else reading_id

    def _change_updated_at(self) -> None:
        self._updated_at = datetime.utcnow()

    def __str__(self) -> str:
        read_at = self.read_at.isoformat() if self.read_at is not None else "-"
        updated_at = self.updated_at.isoformat() if self.updated_at is not None else "-"
        received_at = self.received_at.isoformat() if self.received_at is not None else "-"
        return f"Id: '{self.id}' | Sensor Id: '{self.sensor_id}' | Location Id: '{self.reading_location_id}' | " \
               f"Reading Value: '{self.reading_value}' | Trusted?: {self.is_trusted_reading} | " \
               f"Location Known?: {self.is_location_known} | Location Accurate?: {self.is_location_accurate} | " \
               f"Read at: {read_at} | Updated at: {updated_at} | Received at: {received_at}"

    @property
    def sensor_id(self) -> str:
        return self._sensor_id

    @sensor_id.setter
    def sensor_id(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Sensor Id cannot be null")

        if not isinstance(value, str):
            raise TypeError(f"Sensor Id value must be a string. Got '{type(value).__name__}'")

        self._sensor_id = value

    @property
    def reading_location_id(self) -> str:
        return self._reading_location_id

    @reading_location_id.setter
    def reading_location_id(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Reading Location Id cannot be null")

        if not isinstance(value, str):
            raise TypeError(f"Reading Location Id value must be a string. Got '{type(value).__name__}'")

        self._reading_location_id = value
        self._change_updated_at()

    @property
    def reading_value(self) -> float:
        return self._reading_value

    @reading_value.setter
    def reading_value(self, value: float) -> None:
        if value is None:
            raise ValueError("Reading Value cannot be null")

        if not isinstance(value, float):
            raise TypeError(f"Reading Value must be a float. Got '{type(value).__name__}'")

        self._reading_value = value
        self._change_updated_at()

    @property
    def is_trusted_reading(self) -> bool:
        return self._is_trusted_reading

    @is_trusted_reading.setter
    def is_trusted_reading(self, value: bool) -> None:
        if value is None:
            raise ValueError("Is Trusted Reading flag cannot be null")

        if not isinstance(value, bool):
            raise TypeError(f"Is Trusted Reading flag must be a bool. Got '{type(value).__name__}'")

        self._is_trusted_reading = value
        self._change_updated_at()

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        if value is None or value.strip() == "":
            raise ValueError("Reading Id cannot be null")

        if not isinstance(value, str):
            raise TypeError(f"Reading Id value must be a string. Got '{type(value).__name__}'")

        if not is_valid_guid(value):
            raise ValueError("Reading Id must be a valid guid (UUID4)")

        if self._id is not None and self._id != value:
            raise ValueError(f"Reading Id is set to '{self._id}' and cannot be changed (to '{value}')")

        self._id = value
        self._change_updated_at()

    @property
    def is_location_known(self) -> bool:
        return self._is_location_known

    @is_location_known.setter
    def is_location_known(self, value: bool) -> None:
        if value is None:
            raise ValueError("Is Location Known flag cannot be null")

        if not isinstance(value, bool):
            raise TypeError(f"Is Location Known flag must be a bool. Got '{type(value).__name__}'")

        self._is_location_known = value
        self._change_updated_at()

    @property
    def is_location_accurate(self) -> bool:
        return self._is_location_accurate

    @is_location_accurate.setter
    def is_location_accurate(self, value: bool) -> None:
        if value is None:
            raise ValueError("Is Location Accurate flag cannot be null")

        if not isinstance(value, bool):
            raise TypeError(f"Is Location Accurate flag must be a bool. Got '{type(value).__name__}'")

        self._is_location_accurate = value
        self._change_updated_at()

    @property
    def read_at(self) -> datetime:
        return self._read_at

    @property
    def received_at(self) -> datetime:
        return self._received_at

    @received_at.setter
    def received_at(self, value: datetime) -> None:
        if value is None:
            raise ValueError("Received at datetime cannot be null")

        if not isinstance(value, datetime):
            raise TypeError(f"Received at value must be a datetime. Got '{type(value).__name__}'")

        if self._received_at is not None:
            raise ValueError("Cannot change received at datetime")

        self._received_at = value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @property
    def is_processed(self) -> bool:
        return self._is_processed

    @is_processed.setter
    def is_processed(self, value: bool) -> None:
        if value is None:
            raise ValueError("Is Processed flag cannot be null")

        if not isinstance(value, bool):
            raise TypeError(f"Is Processed flag must be a bool. Got '{type(value).__name__}'")

        self._is_processed = value
        self._change_updated_at()

    @property
    def overall_integrity(self) -> float:
        return self._overall_integrity

    @overall_integrity.setter
    def overall_integrity(self, value: float) -> None:
        if value is None:
            raise ValueError("Overall integrity cannot be null")

        if not isinstance(value, float):
            raise TypeError(f"Overall integrity must be a float. Got '{type(value).__name__}'")

        if value < 0.0 or value > 1.0:
            raise ValueError(f"Overall Integrity must be between 0 (0%) and 1 (100%). Got {value}")

        self._overall_integrity = value


if __name__ == '__main__':
    a = SensorReading("s", "1", 4.20)
