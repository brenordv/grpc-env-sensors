# -*- coding: utf-8 -*-
import grpc
import logging
from datetime import datetime

import server.pb.server_sensors_pb2 as pb2
import server.pb.server_sensors_pb2_grpc as pb2_grpc
from core import converters
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

    def save_new_reading(self,
                         sensor_id: str, reading_location_id: str, reading_value: float, read_at: datetime) -> dict:
        logging.info("[CLIENT] Sending request to save new reading!")
        timer = StopWatch(True)
        reading = converters._from_values_to_proto_new_sensor_reading_save_request(
            sensor_id=sensor_id,
            reading_location_id=reading_location_id,
            reading_value=reading_value,
            read_at=read_at
        )

        response = self.__stub__.save_reading(reading)
        result = {
            "payload": response.reading_id,
            "success": response.result.success,
            "error_message": response.result.error_message
        }

        if response.result.success:
            logging.info("[CLIENT] Success saving new reading.")
        else:
            logging.error(f"[CLIENT] Failed to save new reading. Error: {result['error_message']}")

        logging.info(f"[CLIENT] Saving reading done. Elapsed time: {timer.end()}")
        return result

    def get_readings(self) -> dict:
        logging.info("[CLIENT] Sending request to get all readings!")
        timer = StopWatch(True)
        response = self.__stub__.get_readings(pb2.no_parameter())

        if response.result.success:
            logging.info("[CLIENT] Success getting all readings.")
            payload = [converters._from_proto_sensor_reading_fetch_single_item_response_to_sensor_reading(reading) for
                       reading in response.items]
        else:
            logging.error(f"[CLIENT] Failed to get all readings. Error: {response.result.error_message}")
            payload = None

        logging.info(f"[CLIENT] Get all readings done. Elapsed time: {timer.end()}")
        return {
            "payload": payload,
            "item_count": response.item_count,
            "success": response.result.success,
            "error_message": response.result.error_message
        }

    def get_reading(self, reading_id: str) -> dict:
        logging.info("[CLIENT] Sending request to get all readings!")
        timer = StopWatch(True)

        response = self.__stub__.get_reading(pb2.sensor_reading_fetch_single_item_request(reading_id=reading_id))

        if response.result.success:
            logging.info("[CLIENT] Success getting reading.")
            payload = converters._from_proto_sensor_reading_fetch_single_item_response_to_sensor_reading(response.item)
        else:
            logging.warning(f"[CLIENT] Failed to get reading with id '{reading_id}'. "
                            f"Error: {response.result.error_message}")
            payload = None

        logging.info(f"[CLIENT] Get single reading done. Elapsed time: {timer.end()}")
        return {
            "payload": payload,
            "success": response.result.success,
            "error_message": response.result.error_message
        }
