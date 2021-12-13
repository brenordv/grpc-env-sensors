# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Union

import server.pb.server_sensors_pb2 as pb2
from core.entities.sensor_reading import SensorReading


def iso8601_str_to_datetime(str_dt: str) -> datetime:
    iso8601_format = "%Y-%m-%dT%H:%M:%S.%f"
    return datetime.strptime(str_dt, iso8601_format) if str_dt is not None and str_dt.strip() != "" else None


def from_sensor_reading_to_proto(reading: SensorReading) -> pb2.sensor_reading_item:
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


def from_proto_sensor_reading_request_to_sensor_reading(proto: pb2.sensor_reading_request) -> SensorReading:
    return SensorReading(
        sensor_id=proto.sensor_id,
        reading_location_id=proto.reading_location_id,
        reading_value=proto.reading_value
    )


def from_proto_sensor_reading_item_to_sensor_reading(proto: pb2.sensor_reading_item) -> SensorReading:

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


def from_values_to_sensor_reading(sensor_id: str,
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


def from_values_to_proto_sensor_reading_request(sensor_id: str,
                                                reading_location_id: str,
                                                reading_value: float) -> pb2.sensor_reading_request:
    return pb2.sensor_reading_request(
        sensor_id=sensor_id,
        reading_location_id=reading_location_id,
        reading_value=reading_value
    )
