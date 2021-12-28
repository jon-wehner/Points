"""
Entry file for the points flask application
"""
from flask import Flask, jsonify, request
from app.models import User


app = Flask(__name__)
user = User()

@app.route('/transaction', methods=['POST'])
def transaction():
    """
    Accepts a json string with payer, points, timestamp.
    Calls the method to add transaction to user balance.
    Returns success message or any errors.
    """
    json = request.get_json()
    payer = json['payer']
    points = json['points']
    timestamp = json['timestamp']

    result = user.add_transaction(payer, points, timestamp)

    return jsonify(result)
