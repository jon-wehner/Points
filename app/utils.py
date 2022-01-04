"""
Utility helper functions that can be used in multiple modules
"""
from datetime import datetime

def convert_datestring(datestring):
    """
    Splits a date string to create a new datetime object
    """
    split_datetime= datestring.split('T')

    date = split_datetime[0].split('-')
    date = [int(el) for el in date]

    time = split_datetime[1].split(':')
    time[2] = time[2][0:2]
    time = [int(el) for el in time]

    return datetime(*date, *time)
