# -*- coding: utf-8 -*-
from core.entities.location import Location
from core.entities.sensor import Sensor
from core.services.storage_service import StorageService
from core.settings import configure_application_logging
from server import sensor_server


def add_test_sensors_and_locations():
    """
    Adds a bunch of test data. Since we're passing the Ids, this method can be executed multiple times.
    """
    with StorageService() as storage:
        storage.upsert_location(Location("L0", "Ground Zero"))
        storage.upsert_location(Location("L1", "First Location"))
        storage.upsert_location(Location("L2", "Second Location"))
        storage.upsert_location(Location("L3", "Third Location"))

        storage.upsert_sensor(Sensor("S0", "L0", "First Sensor - Ground Zero"))
        storage.upsert_sensor(Sensor("S4", "L0", "Second Sensor - Ground Zero"))
        storage.upsert_sensor(Sensor("S1", "L1", "First Sensor"))
        storage.upsert_sensor(Sensor("S2", "L2", "Second Sensor"))
        storage.upsert_sensor(Sensor("S3", "L3", "Third Sensor"))

        for s in storage.get_sensors():
            print(s)

        for l in storage.get_locations():
            print(l)


def start_sensor_server():
    """Starts the GRPC server for Sensors."""
    sensor_server.serve()


if __name__ == '__main__':
    configure_application_logging()

    add_test_sensors_and_locations()
    start_sensor_server()
