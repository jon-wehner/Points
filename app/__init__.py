"""
Entry file for the points flask application
"""
from flask import Flask
from datetime import date

app = Flask(__name__)

class User:
    def __init__(self):
        self.transactions = []
        self.balances = {}
    
    def add_transaction(self, payer, points, timestamp):
        new_transaction = { "payer": payer, "points": points, "timestamp": timestamp }
        if self.transactions.length == 0:
            self.transactions.append()
        else:
            index = 0
            while index < self.transactions.length:
                current_transaction = self.transactions[index]
                if new_transaction.timestamp < current_transaction.timestamp:
                    self.transactions.insert(index, new_transaction)
                    break
                index += 1
            self.transactions.append(new_transaction)
        return 'Transaction Successful'
    def _update_balance(self, payer, points):
        if self.balances[payer]:
            self.balances[payer] += points
        else:
            self.balances[payer] = points





@app.route("/")
def hello_world():
    """
    Route Function that Returns hello world statement
    """
    return "<p>Hello, world!</p>"
