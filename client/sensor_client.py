# -*- coding: utf-8 -*-
import logging
from typing import Union, List

import grpc

import server.pb.server_sensors_pb2 as pb2
import server.pb.server_sensors_pb2_grpc as pb2_grpc
from core import converters
from core.entities.sensor_reading import SensorReading
from core.utils import StopWatch


class SensorClient(object):
    def __init__(self, host: str = "localhost", secure_port: int = 50042, insecure_port: int = 50142, credentials=None,
                 use_insecure: bool = True):
        logging.info("[CLIENT] Initializing client...")

        if use_insecure:
            self.__channel__ = grpc.insecure_channel(f"{host}:{insecure_port}")
        else:
            self.__channel__ = grpc.secure_channel(f"{host}:{secure_port}", credentials=credentials)

        self.__stub__ = pb2_grpc.SensorServiceStub(self.__channel__)

    def save_new_reading(self, sensor_id: str, reading_location_id: str, reading_value: float) -> dict:
        logging.info("[CLIENT] Sending request to save new reading!")
        timer = StopWatch(True)
        reading = converters.from_values_to_proto_sensor_reading_request(
            sensor_id=sensor_id,
            reading_location_id=reading_location_id,
            reading_value=reading_value
        )

        response = self.__stub__.save_reading(reading)

        if response.success:
            logging.info("[CLIENT] Success saving new reading.")
        else:
            logging.error(f"[CLIENT] Failed to save new reading. Error: {response.error_message}")

        logging.info(f"[CLIENT] Saving reading done. Elapsed time: {timer.end()}")
        return {
            "payload": response.reading_id,
            "success": response.success,
            "error_message": response.error_message
        }

    def get_readings(self) -> dict:
        logging.info("[CLIENT] Sending request to get all readings!")
        timer = StopWatch(True)
        response = self.__stub__.get_readings(pb2.no_parameter())

        if response.success:
            logging.info("[CLIENT] Success getting all readings.")
            return_payload = [converters.from_proto_sensor_reading_item_to_sensor_reading(reading) for reading in response.sensor_readings]
        else:
            logging.error(f"[CLIENT] Failed to get all readings. Error: {response.error_message}")
            return_payload = None

        logging.info(f"[CLIENT] Get all readings done. Elapsed time: {timer.end()}")
        return {
            "payload": return_payload,
            "success": response.success,
            "error_message": response.error_message
        }

    def get_reading(self, reading_id: str) -> dict:
        logging.info("[CLIENT] Sending request to get all readings!")
        timer = StopWatch(True)

        response = self.__stub__.get_reading(pb2.sensor_reading_fetch_request(reading_id=reading_id))

        if response.success:
            logging.info("[CLIENT] Success getting reading.")
            return_payload = converters.from_proto_sensor_reading_item_to_sensor_reading(response.sensor_reading_item)
        else:
            logging.warning(f"[CLIENT] Failed to get reading with id '{reading_id}'. Error: {response.error_message}")
            return_payload = None

        logging.info(f"[CLIENT] Get single reading done. Elapsed time: {timer.end()}")
        return {
            "payload": return_payload,
            "success": response.success,
            "error_message": response.error_message
        }
