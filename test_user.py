"""
Module for testing the user class
"""
import pytest
from app.models import User

transaction_1 = { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
transaction_2 = { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
transaction_3 = { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" }
transaction_4 = { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }
transaction_5 = { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }

@pytest.fixture
def test_user():
    user = User()
    user.add_transaction(transaction_1["payer"],
        int(transaction_1["points"]), transaction_1["timestamp"])
    user.add_transaction(transaction_2["payer"],
        int(transaction_2["points"]), transaction_2["timestamp"])
    user.add_transaction(transaction_3["payer"],
        int(transaction_3["points"]), transaction_3["timestamp"])
    user.add_transaction(transaction_4["payer"],
        int(transaction_4["points"]), transaction_4["timestamp"])
    user.add_transaction(transaction_5["payer"],
        int(transaction_5["points"]), transaction_5["timestamp"])
    return user

def test_transaction_order(test_user):
    """
    Tests that the add_transaction method correctly updates transaction list
    """
    assert test_user.transactions[1] == transaction_5

def test_balance(test_user):
    assert test_user.balances["DANNON"] == 1100

def test_spend(test_user, points=5000):
    result = test_user.spend_points(points)
    assert result == [
        { "payer": "DANNON", "points": -100 },
        { "payer": "UNILEVER", "points": -200 },
        { "payer": "MILLER COORS", "points": -4700 }
    ]

def test_spend_to_zero(test_user, points=500000):
    result = test_user.spend_points(points)
    assert result == [
        { "payer": "DANNON", "points": -1100 },
        { "payer": "UNILEVER", "points": -200 },
        { "payer": "MILLER COORS", "points": -10000 }
    ] and test_user.balances['MILLER COORS'] == 0
