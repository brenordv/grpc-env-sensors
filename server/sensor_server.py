# -*- coding: utf-8 -*-
import grpc
import logging
from datetime import datetime
from concurrent import futures

import server.pb.server_sensors_pb2 as pb2
import server.pb.server_sensors_pb2_grpc as pb2_grpc
from core.converters import KnownTypes
from core import converters
from core.services.storage_service import StorageService
from core.utils import StopWatch


class SensorServer(pb2_grpc.SensorService):
    def __init__(self):
        logging.info("[SERVER] Starting SensorServer...")
        self._storage_service = StorageService()

    def shutdown(self):
        self._storage_service.close()

    def save_reading(self, request: pb2.new_sensor_reading_save_request, target, options=(),
                     channel_credentials=None, call_credentials=None, insecure=False, compression=None,
                     wait_for_ready=None, timeout=None, metadata=None) -> pb2.new_sensor_reading_save_response:
        timer = StopWatch(True)
        error_msg = ''
        persisted_msg = ''
        try:
            if request is None:
                error_msg = " | Error messages: cannot persist or update a null reading"
                return pb2.new_sensor_reading_save_response(
                    reading_id=None,
                    result=converters.From({
                        "success": False,
                        "error_message": "cannot persist or update a null reading"
                    }).to(KnownTypes.BASE_OPERATION_RESULT)
                )

            timer = StopWatch(True)

            reading = converters.From(request).to(KnownTypes.SENSOR_READING)
            reading.received_at = datetime.utcnow()

            self._storage_service.upsert_reading(reading)

            persisted_msg = f" | Reading: {reading}"

            return pb2.new_sensor_reading_save_response(
                reading_id=reading.id,
                result=converters.build_success_result()
            )

        except Exception as e:
            error_msg = f" | Error messages: {e}"
            raise

        finally:
            logging.info(f"[SERVER] Save reading done. Elapsed time: {timer.end()}{persisted_msg}{error_msg}")

    def get_readings(self,
                     request: pb2.no_parameter, target, options=(),
                     channel_credentials=None, call_credentials=None, insecure=False, compression=None,
                     wait_for_ready=None, timeout=None, metadata=None) -> pb2.sensor_reading_fetch_multi_item_response:
        timer = StopWatch(True)
        error_msg = ''
        read_count = ''

        try:
            readings = self._storage_service.get_readings()
            proto_readings = [converters.From(reading).to(KnownTypes.SENSOR_READING_ITEM) for reading in readings]
            read_count = f" | Found '{len(proto_readings)}' items."

            return pb2.sensor_reading_fetch_multi_item_response(
                items=proto_readings,
                item_count=len(proto_readings),
                result=converters.build_success_result()
            )

        except Exception as e:
            error_msg = f" | Error messages: {e}"
            raise

        finally:
            logging.info(f"[SERVER] Get all readings done. Elapsed time: {timer.end()}{read_count}{error_msg}")

    def get_reading(self, request: pb2.sensor_reading_fetch_single_item_request, target, options=(),
                    channel_credentials=None, call_credentials=None, insecure=False, compression=None,
                    wait_for_ready=None, timeout=None, metadata=None) -> pb2.sensor_reading_fetch_single_item_response:
        timer = StopWatch(True)
        reading_id = request.reading_id
        error_msg = ''
        read_msg = ''

        try:
            if reading_id is None:
                error_msg = " | Error messages: no id was provided to search for sensor reading"
                return pb2.sensor_reading_fetch_single_item_response(
                    item=None,
                    result=converters.From({
                        "success": False,
                        "error_message": "no id was provided to search for sensor reading"
                    }).to(KnownTypes.BASE_OPERATION_RESULT)
                )

            reading = self._storage_service.get_reading(reading_id)
            if reading is None:
                error_msg = " | Error messages: no sensor reading found with id"
                result = pb2.sensor_reading_fetch_single_item_response(
                    item=None,
                    result=converters.From({
                        "success": True,
                        "error_message": f"no sensor reading found with id: '{reading_id}'"
                    }).to(KnownTypes.BASE_OPERATION_RESULT)
                )

            else:
                result_item = converters.From(reading).to(KnownTypes.SENSOR_READING_ITEM)
                result = pb2.sensor_reading_fetch_single_item_response(
                    item=result_item,
                    result=converters.build_success_result()
                )

            read_msg = f" | Read msg: {reading}"
            return result

        except Exception as e:
            error_msg = f" | Error messages: {e}"
            raise

        finally:
            logging.info(f"[SERVER] Getting read with id '{reading_id}' done. Elapsed time: {timer.end()}{read_msg}"
                         f"{error_msg}")


def serve(wait_for_termination: bool = True, max_workers: int = 10, secure_port: int = 50042,
          insecure_port: int = 50142, server_credentials=None):
    sensor_server = SensorServer()
    try:
        timer = StopWatch(True)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        pb2_grpc.add_SensorServiceServicer_to_server(sensor_server, server)

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

    finally:
        sensor_server.shutdown()


if __name__ == '__main__':
    serve()
