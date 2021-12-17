# -*- coding: utf-8 -*-
from datetime import datetime
import requests

from core.settings import SETTINGS


def main():
    result = requests.post(f"http://localhost:{SETTINGS['api']['port']}/sensors/v1",
                           json={
                               "sensor_id": "S1",
                               "reading_location_id": "L1",
                               "reading_value": 42.007,
                               "read_at": datetime.utcnow().isoformat()
                           })

    print(f"[{result.status_code} - {result.reason}] {result.text}")


if __name__ == '__main__':
    main()
