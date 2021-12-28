"""
Entry file for the points flask application
"""
from flask import Flask



app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Route Function that Returns hello world statement
    """
    return "<p>Hello, world!</p>"
