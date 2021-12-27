# -*- coding: utf-8 -*-
import logging
import multiprocessing
from datetime import datetime
from raccoon_simple_stopwatch.stopwatch import StopWatch

from simple_log_factory.log_factory import log_factory
from client.sensor_client import SensorClient


def _save_reading_worker_grpc(num_requests: int, wid: int):
    logger = log_factory(
        log_name=f"WID_{wid:03d}",
        log_level=logging.INFO
    )
    client = SensorClient()
    timer = StopWatch(auto_start=True)

    for i in range(num_requests):
        client.save_new_reading(
            sensor_id="S1",
            reading_location_id="L1",
            reading_value=42,
            read_at=datetime.utcnow()
        )
    logger.info(f"## Worker: {wid} finished! Elapsed time: {timer.end()}")


def _read_reading_worker_grpc(num_requests: int, wid: int, **kwargs):
    logger = log_factory(
        log_name=f"WID_{wid:03d}",
        log_level=logging.INFO
    )
    client = SensorClient()
    timer = StopWatch(auto_start=True)

    for i in range(num_requests):
        client.get_readings(limit=kwargs["limit"])
    logger.info(f"## Worker: {wid} finished! Elapsed time: {timer.end()}")


def _read_reading_by_id_worker_grpc(num_requests: int, wid: int, **kwargs):
    logger = log_factory(
        log_name=f"WID_{wid:03d}",
        log_level=logging.INFO
    )
    client = SensorClient()
    timer = StopWatch(auto_start=True)

    for i in range(num_requests):
        client.get_reading(reading_id=kwargs["reading_id"])

    logger.info(f"## Worker: {wid} finished! Elapsed time: {timer.end()}")


def benchmark_save_reading(num_workers: int, msgs_per_worker: int, worker, **kwargs):
    cpus = multiprocessing.cpu_count()
    timer = StopWatch(auto_start=True)

    print(f"CPUs available: {cpus}")
    print(f"Starting benchmark at: {timer.start_datetime}")

    pool = multiprocessing.Pool()
    for wid in range(num_workers):
        pool.apply_async(worker, args=(msgs_per_worker, wid), kwds=kwargs)

    print("Now waiting...")
    pool.close()
    pool.join()

    elapsed_time = timer.end()
    its = float(msgs_per_worker * num_workers) / float(timer.elapsed(raw=True).total_seconds())
    print(f"All done! Elapsed time: {elapsed_time}. Requests/Sec: {its}")


if __name__ == '__main__':
    benchmark_save_reading(
        num_workers=1000,
        msgs_per_worker=100,
        worker=_read_reading_by_id_worker_grpc,
        reading_id="d764fa3e-753a-4801-9c77-9b9baa1d8bb2"
    )
