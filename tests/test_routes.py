"""
Module for testing the application routes
"""
import pytest
from flask import json
from app import app
from .test_user import transaction_1, transaction_2, transaction_3, transaction_4, transaction_5

@pytest.fixture
def client():
    """
    Sets up test client
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client
@pytest.fixture
def post_transactions(client):
    """
    adds some points to user balance
    """
    client.post('/transaction', json=transaction_1)
    client.post('/transaction', json=transaction_2)
    client.post('/transaction', json=transaction_3)
    client.post('/transaction', json=transaction_4)
    client.post('/transaction', json=transaction_5)


good_transaction = { "payer": "DANNON",
    "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }

def test_successful_transaction(client):
    """
    posts a valid transaction to the transaction route
    """
    response = client.post('/transaction', json=good_transaction)
    data = json.loads(response.data)
    assert data['Message']== 'Transaction Successful'

def test_spend(client, post_transactions):
    """
    tests the app's spend route
    """
    response = client.post('/spend', json={'points' : 5000})
    data = json.loads(response.data)
    dannon = data[0]
    unilever = data[1]
    miller_coors = data[2]
    assert dannon['points'] == -100
    assert unilever['points'] == -200
    assert miller_coors['points'] == -4700

def test_balances(client):
    """
    test app's route to check user balances
    """
    response = client.get('/balances')
    data = json.loads(response.data)
    assert data['DANNON'] == 2000
    assert data['UNILEVER'] == 0
    assert data['MILLER COORS'] == 5300

