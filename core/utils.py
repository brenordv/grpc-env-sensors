# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from timeit import default_timer as timer
from typing import Union


class StopWatch(object):
    """ StopWatch

    A class that manages a StopWatch, so you can easily measure elapsed time of operations.

    Attributes
    ----------
    start_datetime : datetime
        Date and time when the time started.

    end_datetime : datetime
        Date and time when the time stopped.


    Methods
    -------
    start() -> None:
        Starts the timer.

    elapsed(raw: bool = False) -> Union[str, timedelta, None]:
        Returns the current elapsed time.

    end(raw: bool = False) -> Union[str, timedelta, None]:
        Stops the timer and returns the total elapsed time.

    """

    def __init__(self, auto_start: bool = False):
        """
        Creates a new instance of this Stopwatch.

        :param auto_start: if true, will auto start the timer.
        """
        self.__start_timer__ = None
        self.__end_timer__ = None
        self.start_datetime = None
        self.end_datetime = None

        if auto_start:
            self.start()

    def start(self) -> None:
        """
        Starts the timer.
        :return: None
        """
        self.start_datetime = datetime.now()
        self.__start_timer__ = timer()

    def elapsed(self, raw: bool = False) -> Union[str, timedelta, None]:
        """
        Returns the elapsed time either from a current running timer or the total timer,
        if it has been stopped.

        :param raw: if true, will return a timedelta object with the elapsed time.
                    otherwise, will return the string version (days.hours:minutes:seconds.ms)

        :return: elapsed time either in a string or timedelta format.
                 if this method is called before starting the timer, will return None.
        """
        if self.__start_timer__ is None:
            return None

        end = timer() if self.__end_timer__ is None else self.__end_timer__
        elapsed_time = timedelta(seconds=end - self.__start_timer__)

        if raw:
            return elapsed_time
        return str(elapsed_time)

    def end(self, raw: bool = False) -> Union[str, timedelta, None]:
        """
        Stops the current timer.
        If it's called multiple times, after the first call, this method will just
        return the elapsed time. (Same behaviour has elasped() method)

        :param raw: if true, will return a timedelta object with the elapsed time.
                    otherwise, will return the string version (days.hours:minutes:seconds.ms)

        :return: elapsed time either in a string or timedelta format.
        """
        if self.__end_timer__ is not None:
            return self.elapsed(raw=raw)

        self.end_datetime = datetime.now()
        self.__end_timer__ = timer()

        return self.elapsed(raw=raw)


def iso8601_str_to_datetime(str_dt: str) -> datetime:
    iso8601_format = "%Y-%m-%dT%H:%M:%S.%f"
    return datetime.strptime(str_dt, iso8601_format) if str_dt is not None and str_dt.strip() not in ("", "-") else None


def merge_dicts(a: dict, b: dict) -> dict:
    for key, item in a.items():
        if isinstance(item, dict):
            a[key] = merge_dicts(item, b.get(key, {}))
        else:
            val = b.get(key)
            if val is None:
                continue
            a[key] = item

    return a
