# -*- coding: utf-8 -*-
import logging
from datetime import datetime

import grpc
from concurrent import futures

import server.pb.server_sensors_pb2 as pb2
import server.pb.server_sensors_pb2_grpc as pb2_grpc
from core import converters
from core.services.storage_service import StorageService
from core.utils import StopWatch


class SensorServer(pb2_grpc.SensorService):
    def __init__(self):
        logging.info("[SERVER] Starting SensorServer...")
        self._storage_service_ = StorageService()

    def save_reading(self, request: pb2.sensor_reading_request, target, options=(),
                     channel_credentials=None, call_credentials=None, insecure=False, compression=None,
                     wait_for_ready=None, timeout=None, metadata=None):
        if request is None:
            return pb2.sensor_reading_response(
                reading_id=None,
                success=False,
                error_message="Cannot persist or update a null reading"
            )
        logging.info("[SERVER] Save reading requested!")
        timer = StopWatch(True)
        reading = converters.from_proto_sensor_reading_request_to_sensor_reading(request)
        reading.received_at = datetime.utcnow()

        logging.info(f"[SERVER] Persisting reading: {reading}")
        self._storage_service_.upsert_reading(reading)

        logging.info(f"[SERVER] Save reading done. Elapsed time: {timer.end()}")
        return pb2.sensor_reading_response(
            reading_id=reading.id,
            success=True,
            error_message=None
        )

    def get_readings(self,
                     request: pb2.no_parameter, target, options=(),
                     channel_credentials=None, call_credentials=None, insecure=False, compression=None,
                     wait_for_ready=None, timeout=None, metadata=None):
        logging.info("[SERVER] Get all readings requested!")
        timer = StopWatch(True)
        readings = self._storage_service_.get_readings()
        proto_readings = [converters.from_sensor_reading_to_proto(reading) for reading in readings]
        logging.info(f"[SERVER] Get all readings done. Elapsed time: {timer.end()}")
        return pb2.sensor_reading_fetch_response(
            sensor_readings=proto_readings,
            success=True,
            error_message=None
        )

    def get_reading(self, request: pb2.sensor_reading_fetch_request, target, options=(),
                    channel_credentials=None, call_credentials=None, insecure=False, compression=None,
                    wait_for_ready=None, timeout=None, metadata=None):
        logging.info(f"[SERVER] Get reading by id requested!")
        timer = StopWatch(True)
        reading_id = request.reading_id

        if reading_id is None:
            return pb2.sensor_reading_fetch_item_response(
                sensor_reading_item=None,
                success=False,
                error_message="No id was provided to search for sensor reading"
            )

        reading = self._storage_service_.get_reading(reading_id)
        if reading is None:
            result = pb2.sensor_reading_fetch_item_response(
                sensor_reading_item=None,
                success=False,
                error_message=f"No sensor reading found with id: '{reading_id}'"
            )

        else:
            result = pb2.sensor_reading_fetch_item_response(
                sensor_reading_item=converters.from_sensor_reading_to_proto(reading),
                success=True,
                error_message=None
            )

        logging.info(f"[SERVER] Getting single reading done. Elapsed time: {timer.end()}")
        return result


def serve(wait_for_termination: bool = True, max_workers: int = 10, secure_port: int = 50042,
          insecure_port: int = 50142, server_credentials=None):
    timer = StopWatch(True)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    pb2_grpc.add_SensorServiceServicer_to_server(SensorServer(), server)

    if insecure_port is not None:
        server.add_insecure_port(f"[::]:{insecure_port}")

    elif secure_port is not None and server_credentials is not None:
        server.add_secure_port(f"[::]:{secure_port}", server_credentials=server_credentials)

    else:
        raise ValueError("Could not figure ou which tpe of connection to use (secure or insecure)")

    logging.info("[SERVER] Starting server...")
    server.start()

    logging.info("[SERVER] Server is working and waiting for requests...")
    logging.info(f"[SERVER] Startup time: {timer.end()}")
    if wait_for_termination:
        logging.info("[SERVER] Server is also standing by and waiting for termination...")
        server.wait_for_termination()


if __name__ == '__main__':
    serve()
