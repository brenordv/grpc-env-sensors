# -*- coding: utf-8 -*-
from core.services.storage_service import StorageService


def get_readings_without_id():
    st = StorageService()
    invalid_readings = []
    for reading in st.get_readings(limit=None):
        if reading.id is not None:
            continue
        invalid_readings.append(reading)
        print(f"Reading found without Id: {reading}")

    invalid_count = len(invalid_readings)
    if invalid_count == 0:
        print("No invalid readings found...")
    else:
        print(f"Found {invalid_count} invalid readings...")


if __name__ == '__main__':
    get_readings_without_id()
