# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from typing import Union, Generator
import ZODB
import ZODB.FileStorage
import transaction
from persistent.mapping import PersistentMapping

from core.entities.location import Location
from core.entities.sensor import Sensor
from core.entities.sensor_reading import SensorReading
from core.settings import DB_FILE


class StorageService(object):
    """
    StorageService has all the methods to handle persistence of all entities of this application.
    Yes, it's a bloated, unsustainable approach (in the long run), but works just fine for this demo.
    """
    def __init__(self, db_file: Union[str, Path] = DB_FILE):
        storage = ZODB.FileStorage.FileStorage(str(db_file))
        self._db = ZODB.DB(storage)
        self._connection = self._db.open()
        self._root = self._connection.root()

        self._locations_key = "locations"
        self._sensor_readings_key = "sensor_readings"
        self._sensors_key = "sensors"

        for db_name in [self._locations_key, self._sensor_readings_key, self._sensors_key]:
            if db_name in self._root:
                continue
            logging.info(f"Creating collection: {db_name}")
            self._root[db_name] = PersistentMapping()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        transaction.commit()
        self._db.close()
        self._connection.close()

    def get_location(self, location_id: str) -> Union[Location, None]:
        """Returns a single location (or null if it doesn't exist)."""
        fetched_location = self._root[self._locations_key].get(location_id)
        return fetched_location

    def get_locations(self) -> Generator[Location, None, None]:
        """Returns all registered locations."""
        for _, location in self._root[self._locations_key].items():
            yield location

    def get_sensor(self, sensor_id: str) -> Union[Sensor, None]:
        """Returns a single sensor (or null if it doesn't exist)."""
        fetched_sensor = self._root[self._sensors_key].get(sensor_id)
        return fetched_sensor

    def get_sensors(self) -> Generator[Sensor, None, None]:
        """Returns all registered sensors."""
        for _, sensor in self._root[self._sensors_key].items():
            yield sensor

    def get_reading(self, reading_id: str) -> Union[SensorReading, None]:
        """Returns a single sensor reading (or null if it doesn't exist)."""
        fetched_reading = self._root[self._sensor_readings_key].get(reading_id)
        return fetched_reading

    def get_readings(self) -> Generator[SensorReading, None, None]:
        """Returns all registered sensor readings."""
        for reading_id, reading in self._root[self._sensor_readings_key].items():
            yield reading

    def upsert_location(self, location: Location) -> None:
        """Inserts or update a location."""
        if location is None:
            raise ValueError(f"Cannot add or update a null location")

        self._root[self._locations_key][location.id] = location
        transaction.commit()

    def upsert_sensor(self, sensor: Sensor) -> None:
        """Inserts or update a sensor."""
        if sensor is None:
            raise ValueError(f"Cannot add or update a null sensor")

        self._root[self._sensors_key][sensor.id] = sensor
        transaction.commit()

    def upsert_reading(self, reading: SensorReading) -> None:
        """Inserts or update a sensor reading."""
        if reading is None:
            raise ValueError(f"Cannot add or update a null reading")

        validated_reading = self.check_reading_integrity(reading)

        self._root[self._sensor_readings_key][validated_reading.id] = validated_reading
        transaction.commit()

    def check_reading_integrity(self, reading: SensorReading) -> SensorReading:
        """Makes a bunch of validations on the reading, to check its validity.
        :returns: Updated sensor reading.
        """
        reading.is_trusted_reading = self.check_is_sensor_trusted(reading.sensor_id)
        reading.is_location_known = self.check_is_location_known(reading.reading_location_id)
        reading.is_location_accurate = self.check_is_location_accurate(reading.sensor_id, reading.reading_location_id)

        check_results = [reading.is_trusted_reading, reading.is_location_known, reading.is_location_accurate]
        checks_passed = [result for result in check_results if result]

        reading.overall_integrity = float(len(checks_passed)) / float(len(check_results))

        return reading

    def check_is_sensor_trusted(self, sensor_id: str) -> bool:
        """
        Checks if the sensor id represents a known sensor.
        In this case, known and trusted are synonyms.
        """
        # This could use a memory cache to improve performance... maybe?
        return self.get_sensor(sensor_id) is not None

    def check_is_location_known(self, location_id: str) -> bool:
        """Checks if the location id represents a known location."""
        # This could use a memory cache to improve performance... maybe?
        return self.get_location(location_id) is not None

    def check_is_location_accurate(self, sensor_id: str, location_id: str) -> bool:
        """
        Checks if the location is  accurate.
        To be accurate, the location provided in the reading must be the same in the sensor.
        """
        # This could use a memory cache to improve performance... maybe?
        sensor = self.get_sensor(sensor_id)
        if sensor is None:
            raise ValueError(f"No sensor found with id '{sensor_id}'")

        return sensor.location_id == location_id
