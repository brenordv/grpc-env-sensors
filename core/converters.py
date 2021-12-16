# -*- coding: utf-8 -*-
from datetime import datetime
from enum import Enum
from typing import Union

import server.pb.server_sensors_pb2 as pb2
from core.entities.sensor_reading import SensorReading
from core.utils import iso8601_str_to_datetime


class OperationTypes(Enum):
    request = 1
    response = 2


class KnownTypes(Enum):
    values = 1
    sensor_reading = 2
    sensor_reading_item = 3
    new_sensor_reading_save_request = 4
    base_operation_result = 5


class ConvertOperations(Enum):
    new_reading_request = 1
    new_reading_response = 2
    read_one_request = 3
    read_one_response = 4
    read_multi_request = 5
    read_multi_response = 6
    sensor_reading_entity = 7


class From(object):
    def __init__(self, input_value):
        self._type = self._get_conversion_type(input_value)
        self._value = input_value

    @staticmethod
    def _get_conversion_type(input_value) -> KnownTypes:
        if isinstance(input_value, dict):
            return KnownTypes.values

        elif isinstance(input_value, SensorReading):
            return KnownTypes.sensor_reading

        elif isinstance(input_value, pb2.sensor_reading_item):
            return KnownTypes.sensor_reading_item

        elif isinstance(input_value, pb2.new_sensor_reading_save_request):
            return KnownTypes.new_sensor_reading_save_request

        raise TypeError(f"type '{type(input_value).__name__}' is unknown")

    def to(self, new_type: KnownTypes):
        if self._type == KnownTypes.values and new_type == KnownTypes.sensor_reading:
            return _from_values_to_sensor_reading(**self._value)

        elif self._type == KnownTypes.values and new_type == KnownTypes.new_sensor_reading_save_request:
            return _from_values_to_proto_new_sensor_reading_save_request(**self._value)

        elif self._type == KnownTypes.values and new_type == KnownTypes.base_operation_result:
            return _from_values_to_proto_base_operation_result(**self._value)

        elif self._type == KnownTypes.sensor_reading_item and new_type == KnownTypes.sensor_reading:
            return _from_proto_sensor_reading_fetch_single_item_response_to_sensor_reading(self._value)

        elif self._type == KnownTypes.new_sensor_reading_save_request and new_type == KnownTypes.sensor_reading:
            return _from_proto_new_sensor_reading_save_request_to_sensor_reading(self._value)

        elif self._type == KnownTypes.sensor_reading and new_type == KnownTypes.sensor_reading_item:
            return _from_sensor_reading_to_proto_sensor_reading_fetch_multi_item_response(self._value)

        raise TypeError(f"don't know how to convert from '{self._type}' to '{new_type}'")


def build_success_result():
    return From({
        "success": True,
        "error_message": None
    }).to(KnownTypes.base_operation_result)


def _from_sensor_reading_to_proto_sensor_reading_fetch_multi_item_response(
        reading: SensorReading) -> pb2.sensor_reading_item:
    return pb2.sensor_reading_item(
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


def _from_proto_sensor_reading_fetch_single_item_response_to_sensor_reading(
        proto: pb2.sensor_reading_item) -> SensorReading:
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
