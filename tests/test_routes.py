"""
Module for testing the application routes
"""
import pytest
from flask import json, jsonify
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

good_transaction = { "payer": "DANNON",
    "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }

def test_successful_transaction(client):
    response = client.post('/transaction', json=good_transaction)
    data = json.loads(response.data)
    assert data['Message']== 'Transaction Successful'
    
