# -*- coding: utf-8 -*-
from typing import Generator

from core.services.storage_service import StorageService


def main():
    with StorageService() as storage:
        _print("Sensors", storage.get_sensors())
        print()
        _print("Locations", storage.get_locations())


def _print(label: str, objects: Generator[any, None, None]) -> None:
    printed = 0
    print(f"########## {label}")
    for obj in objects:
        print(obj)
        printed += 1

    if printed == 0:
        print(f"--- No '{label}' found.")
    else:
        print(f"--- Found {printed} '{label}'.")


if __name__ == '__main__':
    main()

