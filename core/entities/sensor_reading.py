# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from typing import Union

from core import validators


class SensorReading(object):
    # Id
    _id: Union[str, None] = None

    # Required values
    _sensor_id: Union[str, None] = None
    _reading_location_id: Union[str, None] = None
    _reading_value: Union[float, None] = None

    # Optional or automatic properties
    _is_trusted_reading: bool = False
    _is_location_known: bool = False
    _is_location_accurate: bool = False
    _is_processed: bool = False
    _overall_integrity: float = -1.0
    _read_at: Union[datetime, None] = None
    _received_at: Union[datetime, None] = None
    _updated_at: Union[datetime, None] = None

    def __init__(self,
                 sensor_id: str,
                 reading_location_id: str,
                 reading_value: float,
                 reading_id: Union[str, None] = None,
                 trusted_reading: bool = False,
                 location_known: bool = False,
                 location_accurate: bool = False,
                 is_processed: bool = False,
                 overall_integrity: float = 0.0,
                 read_at: Union[datetime, None] = None,
                 received_at: Union[datetime, None] = None,
                 updated_at: Union[datetime, None] = None):

        self.id = self._generate_id() if reading_id is None else reading_id

        self.sensor_id = sensor_id
        self.reading_location_id = reading_location_id
        self.reading_value = reading_value

        self.is_trusted_reading = trusted_reading
        self.is_location_known = location_known
        self.is_location_accurate = location_accurate
        self.is_processed = is_processed
        self.overall_integrity = overall_integrity

        self._read_at = read_at
        if received_at is not None:
            self.received_at = received_at
        self._set_updated_at(updated_at)

    @staticmethod
    def _generate_id() -> str:
        return str(uuid.uuid4())

    def _set_updated_at(self, dt: datetime) -> None:
        self._updated_at = dt if dt is not None else datetime.utcnow()

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
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        label = "reading id"
        validators.is_str_not_null_or_empty(value, label)
        validators.is_valid_guid(value, label)

        if self._id is not None and self._id != value:
            raise ValueError(f"Reading Id is set to '{self._id}' and cannot be changed (to '{value}')")

        self._id = value
        self._change_updated_at()

    @property
    def sensor_id(self) -> str:
        return self._sensor_id

    @sensor_id.setter
    def sensor_id(self, value: str) -> None:
        label = "sensor id"
        validators.is_str_not_null_or_empty(value, label)

        self._sensor_id = value

    @property
    def reading_location_id(self) -> str:
        return self._reading_location_id

    @reading_location_id.setter
    def reading_location_id(self, value: str) -> None:
        label = "reading location id"
        validators.is_str_not_null_or_empty(value, label)

        self._reading_location_id = value
        self._change_updated_at()

    @property
    def reading_value(self) -> float:
        return self._reading_value

    @reading_value.setter
    def reading_value(self, value: float) -> None:
        label = "reading value"
        validators.is_not_null(value, label)
        validators.is_of_type(value, float, label)

        self._reading_value = value
        self._change_updated_at()

    @property
    def is_trusted_reading(self) -> bool:
        return self._is_trusted_reading

    @is_trusted_reading.setter
    def is_trusted_reading(self, value: bool) -> None:
        label = "is trusted reading"
        validators.is_not_null(value, label)
        validators.is_of_type(value, bool, label)

        self._is_trusted_reading = value
        self._change_updated_at()

    @property
    def is_location_known(self) -> bool:
        return self._is_location_known

    @is_location_known.setter
    def is_location_known(self, value: bool) -> None:
        label = "is location known flag"
        validators.is_not_null(value, label)
        validators.is_of_type(value, bool, label)

        self._is_location_known = value
        self._change_updated_at()

    @property
    def is_location_accurate(self) -> bool:
        return self._is_location_accurate

    @is_location_accurate.setter
    def is_location_accurate(self, value: bool) -> None:
        label = "is location accurate flag"
        validators.is_not_null(value, label)
        validators.is_of_type(value, bool, label)

        self._is_location_accurate = value
        self._change_updated_at()

    @property
    def is_processed(self) -> bool:
        return self._is_processed

    @is_processed.setter
    def is_processed(self, value: bool) -> None:
        label = "is processed flag"
        validators.is_not_null(value, label)
        validators.is_of_type(value, bool, label)

        self._is_processed = value
        self._change_updated_at()

    @property
    def overall_integrity(self) -> float:
        return self._overall_integrity

    @overall_integrity.setter
    def overall_integrity(self, value: float) -> None:
        label = "overall integrity"
        validators.is_not_null(value, label)
        validators.is_of_type(value, float, label)
        validators.is_number_between(value, 0.0, 1.0, label)

        self._overall_integrity = value

    @property
    def read_at(self) -> datetime:
        return self._read_at

    @property
    def received_at(self) -> datetime:
        return self._received_at

    @received_at.setter
    def received_at(self, value: datetime) -> None:
        label = "received at timestamp"
        validators.is_not_null(value, label)
        validators.is_of_type(value, datetime, label)

        if self._received_at is not None:
            raise ValueError("Cannot change received at datetime")

        self._received_at = value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at


def materialize(doc: dict) -> SensorReading:
    return SensorReading(
        reading_id=doc["_id"],
        sensor_id=doc["_sensor_id"],
        reading_location_id=doc["_reading_location_id"],
        reading_value=doc["_reading_value"],
        trusted_reading=doc["_is_trusted_reading"],
        location_known=doc["_is_location_known"],
        location_accurate=doc["_is_location_accurate"],
        is_processed=doc["_is_processed"],
        overall_integrity=doc["_overall_integrity"],
        read_at=doc["_read_at"],
        received_at=doc["_received_at"],
        updated_at=doc["_updated_at"]
    )
