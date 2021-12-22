# -*- coding: utf-8 -*-
from datetime import datetime
from enum import Enum
from typing import Union
import dateutil.parser

import server.pb.server_sensors_pb2 as pb2
from core.entities.sensor_reading import SensorReading
from core.utils import iso8601_str_to_datetime


class KnownTypes(Enum):
    STRING = 1
    INT = 2
    FLOAT = 3
    VALUES = 4
    SENSOR_READING = 5
    SENSOR_READING_MESSAGE = 6
    NEW_SENSOR_READING_SAVE_REQUEST = 7
    BASE_OPERATION_RESULT = 8


class From(object):
    _simple_to_string_types = [KnownTypes.STRING, KnownTypes.INT, KnownTypes.FLOAT, KnownTypes.VALUES]

    def __init__(self, input_value):
        self._type = self._get_conversion_type(input_value)
        self._value = input_value

    @staticmethod
    def _get_conversion_type(input_value) -> KnownTypes:
        if isinstance(input_value, str):
            return KnownTypes.STRING

        elif isinstance(input_value, int):
            return KnownTypes.INT

        elif isinstance(input_value, float):
            return KnownTypes.FLOAT

        elif isinstance(input_value, dict):
            return KnownTypes.VALUES

        elif isinstance(input_value, SensorReading):
            return KnownTypes.SENSOR_READING

        elif isinstance(input_value, pb2.sensor_reading_message):
            return KnownTypes.SENSOR_READING_MESSAGE

        elif isinstance(input_value, pb2.new_sensor_reading_save_request):
            return KnownTypes.NEW_SENSOR_READING_SAVE_REQUEST

        raise TypeError(f"type '{type(input_value).__name__}' is unknown")

    def _from_string(self, new_type: KnownTypes):
        if new_type == KnownTypes.INT:
            return _from_string_to_int(self._value)

        elif new_type == KnownTypes.FLOAT:
            return _from_string_to_float(self._value)

        return None

    def _from_simple_to_str(self, new_type: KnownTypes):
        if new_type == KnownTypes.STRING:
            return _simple_to_string(self._value)

        return None

    def _from_values(self, new_type: KnownTypes):
        if new_type == KnownTypes.SENSOR_READING:
            return _from_values_to_sensor_reading(**self._value)

        elif new_type == KnownTypes.NEW_SENSOR_READING_SAVE_REQUEST:
            return _from_values_to_proto_new_sensor_reading_save_request(**self._value)

        elif new_type == KnownTypes.BASE_OPERATION_RESULT:
            return _from_values_to_proto_base_operation_result(**self._value)

        return None

    def _from_sensor_reading_message(self, new_type: KnownTypes):
        if new_type == KnownTypes.SENSOR_READING:
            return _from_proto_sensor_reading_message_to_sensor_reading(self._value)

        return None

    def _from_new_sensor_reading_request(self, new_type: KnownTypes):
        if new_type == KnownTypes.SENSOR_READING:
            return _from_proto_new_sensor_reading_save_request_to_sensor_reading(self._value)

        return None

    def _from_sensor_reading(self, new_type: KnownTypes):
        if new_type == KnownTypes.SENSOR_READING_MESSAGE:
            return _from_sensor_reading_to_proto_sensor_reading_message(self._value)

        return None

    def to(self, new_type: KnownTypes):
        converted = None
        if self._type == KnownTypes.STRING:
            converted = self._from_string(new_type)

        elif self._type == KnownTypes.VALUES:
            converted = self._from_values(new_type)

        elif self._type == KnownTypes.SENSOR_READING_MESSAGE:
            converted = self._from_sensor_reading_message(new_type)

        elif self._type == KnownTypes.NEW_SENSOR_READING_SAVE_REQUEST:
            converted = self._from_new_sensor_reading_request(new_type)

        elif self._type == KnownTypes.SENSOR_READING:
            converted = self._from_sensor_reading(new_type)

        elif self._type in self._simple_to_string_types:
            converted = self._from_simple_to_str(new_type)

        if converted is None:
            raise TypeError(f"don't know how to convert from '{self._type}' to '{new_type}'")

        return converted


def build_success_result():
    return From({
        "success": True,
        "error_message": None
    }).to(KnownTypes.BASE_OPERATION_RESULT)


def _from_string_to_int(value: str) -> int:
    return int(value)


def _from_string_to_float(value: str) -> float:
    return float(value)


def _simple_to_string(value) -> str:
    return str(value)


def _from_sensor_reading_to_proto_sensor_reading_message(
        reading: SensorReading) -> pb2.sensor_reading_message:
    return pb2.sensor_reading_message(
        id=reading.id,
        sensor_id=reading.sensor_id,
        reading_location_id=reading.reading_location_id,
        reading_value=reading.reading_value,
        trusted_reading=reading.is_trusted_reading,
        location_known=reading.is_location_known,
        location_accurate=reading.is_location_accurate,
        is_processed=reading.is_processed,
        overall_integrity=reading.overall_integrity,
        read_at=reading.read_at.isoformat() if reading.read_at is not None else None,
        updated_at=reading.updated_at.isoformat() if reading.updated_at is not None else None,
        received_at=reading.received_at.isoformat() if reading.received_at is not None else None,
    )


def _from_proto_new_sensor_reading_save_request_to_sensor_reading(
        proto: pb2.new_sensor_reading_save_request) -> SensorReading:
    return SensorReading(
        sensor_id=proto.sensor_id,
        reading_location_id=proto.reading_location_id,
        reading_value=proto.reading_value,
        read_at=iso8601_str_to_datetime(proto.read_at),
    )


def _from_proto_sensor_reading_message_to_sensor_reading(
        proto: pb2.sensor_reading_message) -> SensorReading:
    return SensorReading(
        reading_id=proto.id,
        sensor_id=proto.sensor_id,
        reading_location_id=proto.reading_location_id,
        reading_value=proto.reading_value,
        trusted_reading=proto.trusted_reading,
        location_known=proto.location_known,
        location_accurate=proto.location_accurate,
        is_processed=proto.is_processed,
        overall_integrity=proto.overall_integrity,
        read_at=iso8601_str_to_datetime(proto.read_at),
        updated_at=iso8601_str_to_datetime(proto.updated_at),
        received_at=iso8601_str_to_datetime(proto.received_at)
    )


def _from_values_to_sensor_reading(sensor_id: str,
                                   reading_location_id: str,
                                   reading_value: float,
                                   trusted_reading: bool = False,
                                   location_known: bool = False,
                                   location_accurate: bool = False,
                                   is_processed: bool = False,
                                   overall_integrity: float = 0,
                                   reading_id: Union[str, None] = None,
                                   read_at: Union[datetime, None] = None,
                                   received_at: Union[datetime, None] = None,
                                   updated_at: Union[datetime, None] = None) -> SensorReading:
    return SensorReading(
        sensor_id=sensor_id,
        reading_location_id=reading_location_id,
        reading_value=reading_value,
        trusted_reading=trusted_reading,
        location_known=location_known,
        location_accurate=location_accurate,
        is_processed=is_processed,
        reading_id=reading_id,
        read_at=read_at,
        received_at=received_at,
        updated_at=updated_at,
        overall_integrity=overall_integrity
    )


def _from_values_to_proto_new_sensor_reading_save_request(sensor_id: str,
                                                          reading_location_id: str,
                                                          reading_value: float,
                                                          read_at: datetime) -> pb2.new_sensor_reading_save_request:
    if isinstance(read_at, str):
        read_at = dateutil.parser.isoparse(read_at)

    return pb2.new_sensor_reading_save_request(
        sensor_id=sensor_id,
        reading_location_id=reading_location_id,
        reading_value=reading_value,
        read_at=read_at.isoformat() if read_at is not None else None
    )


def _from_values_to_proto_base_operation_result(
        success: bool = True, error_message: str = None) -> pb2.base_operation_result:
    return pb2.base_operation_result(
        success=success,
        error_message=error_message
    )
