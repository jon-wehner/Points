"""
Module for testing utility functions
"""
from datetime import datetime
import pytest
from app.utils import convert_datestring

TEST_DATE = "2020-11-02T14:00:00Z"

def test_datestring_converstion():
    """
    Tests that the string successfully converted to a datetime object
    """
    result = convert_datestring(TEST_DATE)
    assert isinstance(result, datetime)
