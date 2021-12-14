# -*- coding: utf-8 -*-
import random
from client.sensor_client import SensorClient
from core.settings import configure_application_logging


def send_readings():
    client = SensorClient()
    for i in range(5):
        sensor_id = f"S{i}"
        location_id = f"L{i}"
        reading_value = random.uniform(0.42, 10.77)
        print(f"Adding -- sensor_id: {sensor_id} | location_id: {location_id} | value: {reading_value}", end="")
        result = client.save_new_reading(
            sensor_id=sensor_id,
            reading_location_id=location_id,
            reading_value=reading_value
        )

        print(f" | Success: {result.get('success', 'Not found')} -- Reading Id: {result.get('payload', 'no payload')}")


def get_all_readings():
    client = SensorClient()
    result = client.get_readings()
    print(f"Success: {result['success']}")
    if not result['success']:
        print(f"Error message: {result['error_message']}")
    else:
        for reading in result["payload"]:
            print(reading)


if __name__ == '__main__':
    configure_application_logging()
    send_readings()
    get_all_readings()