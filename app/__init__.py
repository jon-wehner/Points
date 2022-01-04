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
@app.route('/spend', methods=['POST'])
def spend():
    """
    Accepts json string with a points value.
    Calls spend method on the current user.
    Returns amount of points spent or any errors. 
    """
    json = request.get_json()
    points = json['points']

    result = user.spend_points(points)

    return jsonify(result)
@app.route('/balances')
def balances():
    """
    Accepts get requests and returns user balances
    """    
    return jsonify(user.balances)
