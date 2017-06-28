# coding: utf-8

import pytz
from datetime import datetime


def get_current_datetime(format, time_zone="UTC"):
    """
    Get current datetime
    :param format: string, the datetime string format
    :param time_zone: string, the time zone name.
    :return: string, the datetime string
    :example
        get_current_dateime("%Y-%m-%d %H:%M", "UTC")
        2016-05-20 15:55
    """
    return datetime.now(tz=pytz.timezone(time_zone)).strftime(format=format)


def convert_string_to_datetime(date_string, format):
    """
    Convert datetime string to datetime
    :return:
    """
    try:
        return datetime.strptime(date_string, format)
    except:
        raise Exception("fail to convert string '%s' to datetime with format '%s'" % (date_string, format))