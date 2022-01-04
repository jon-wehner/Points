"""
Module for testing utility functions
"""
from datetime import datetime
from app.utils import convert_datestring

TEST_DATE = "2020-11-02T14:00:00Z"

def test_datestring_conversion():
    """
    Tests that the string successfully converted to a datetime object
    """
    result = convert_datestring(TEST_DATE)
    assert isinstance(result, datetime)
    assert result.year == 2020
    assert result.month == 11
    assert result.day == 2
    assert result.hour == 14
    assert result.minute == 0
    assert result.second == 0
