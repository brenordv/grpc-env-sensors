# -*- coding: utf-8 -*-
from typing import Union, Generator
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database

from core.entities import location as location_utils
from core.entities import sensor as sensor_utils
from core.entities import sensor_reading as sensor_reading_utils
from core.entities.location import Location
from core.entities.sensor import Sensor
from core.entities.sensor_reading import SensorReading
from core.settings import SECRETS


class StorageService(object):
    _id_key = "_id"

    """
    StorageService has all the methods to handle persistence of all entities of this application.
    Yes, it's a bloated, unsustainable approach (in the long run), but works just fine for this demo.
    """

    def __init__(self):
        # Just a reminder: Don't do this type of thing. Use a KeyVault of some sort...
        conn_string = SECRETS["connection_strings"]["mongodb_primary"]
        client = pymongo.MongoClient(conn_string)

        self._db: Database = client["envDatabase"]
        self._sensors: Collection = self._db["sensors"]
        self._locations: Collection = self._db["locations"]
        self._readings: Collection = self._db["readings"]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        pass

    @staticmethod
    def _get_one(col: Collection, find_op: dict):
        found = col.find_one(find_op)
        return found

    def _get_all(self, col: Collection, limit: Union[int, None] = 0):
        if limit is None:
            limit = 0

        if limit < 0:
            sort = [(self._id_key, pymongo.DESCENDING), ]
            limit *= -1
        else:
            sort = None

        for doc in col.find(filter=None, sort=sort, limit=limit):
            yield doc

    @staticmethod
    def _upsert(col: Collection, find_op: dict, doc):
        col.replace_one(find_op, doc.__dict__, upsert=True)

    def get_location(self, location_id: str) -> Union[Location, None]:
        """Returns a single location (or null if it doesn't exist)."""
        found = self._get_one(self._locations, {self._id_key: location_id})
        if found is None:
            return None
        return location_utils.materialize(found)

    def get_locations(self) -> Generator[Location, None, None]:
        """Returns all registered locations."""
        for loc in self._get_all(self._locations):
            yield location_utils.materialize(loc)

    def get_sensor(self, sensor_id: str) -> Union[Sensor, None]:
        """Returns a single sensor (or null if it doesn't exist)."""
        found = self._get_one(self._sensors, {self._id_key: sensor_id})
        if found is None:
            return None
        return sensor_utils.materialize(found)

    def get_sensors(self) -> Generator[Sensor, None, None]:
        """Returns all registered sensors."""
        for sen in self._get_all(self._sensors):
            yield sensor_utils.materialize(sen)

    def get_reading(self, reading_id: str) -> Union[SensorReading, None]:
        """Returns a single sensor reading (or null if it doesn't exist)."""
        found = self._get_one(self._readings, {self._id_key: reading_id})
        if found is None:
            return None
        return sensor_reading_utils.materialize(found)

    def get_readings(self, limit: Union[int, None]) -> Generator[SensorReading, None, None]:
        """Returns all registered sensor readings."""
        for sen in self._get_all(self._readings, limit=limit):
            yield sensor_reading_utils.materialize(sen)

    def upsert_location(self, location: Location) -> None:
        """Inserts or update a location."""
        if location is None:
            raise ValueError(f"Cannot add or update a null location")

        self._upsert(self._locations, {self._id_key: location.id}, location)

    def upsert_sensor(self, sensor: Sensor) -> None:
        """Inserts or update a sensor."""
        if sensor is None:
            raise ValueError(f"Cannot add or update a null sensor")

        self._upsert(self._sensors, {self._id_key: sensor.id}, sensor)

    def upsert_reading(self, reading: SensorReading) -> None:
        """Inserts or update a sensor reading."""
        if reading is None:
            raise ValueError(f"Cannot add or update a null reading")

        validated_reading = self.check_reading_integrity(reading)
        self._upsert(self._readings, {self._id_key: validated_reading.id}, validated_reading)

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
