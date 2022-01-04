"""
Module containing the user model
"""
from app.utils import convert_datestring

class User:
    """
    User class that tracks transactions list and balances dictionary.
    """
    def __init__(self):
        self.transactions = []
        self.balances = {}

    def add_transaction(self, payer, points, timestamp):
        """
        Public method for adding a transaction to the user's account.
        Takes payer, points, timestamp as parameters.
        Inserts into the transaction list by ascending date order.
        """
        new_transaction = { 'payer': payer, 'points': points, 'timestamp': timestamp}
        new_transaction_time = convert_datestring(new_transaction['timestamp'])

        if len(self.transactions) == 0:
            self.transactions.append(new_transaction)
        else:
            index = 0
            while index < len(self.transactions):
                current_transaction = self.transactions[index]
                current_transaction_time = convert_datestring(current_transaction['timestamp'])

                if new_transaction_time < current_transaction_time:
                    self.transactions.insert(index, new_transaction)
                    break
                index += 1
            if index == len(self.transactions) - 1:
                self.transactions.append(new_transaction)
        self._update_balance(payer, points)
        return { 'Message' : 'Transaction Successful'}

    def spend_points(self, points):
        """
        Method for spending points balance
        """
        balances = self.balances
        result = {}
        remaining_points = points
        while remaining_points > 0 and len(self.transactions) > 0:
            payment = self.transactions[0]
            points_to_spend = payment['points']
            payer = payment['payer']
            payer_balance = balances[payer]
            spent = 0
            if points_to_spend <= remaining_points and payer_balance >= points_to_spend:
                remaining_points -= points_to_spend
                spent -= points_to_spend
                self.transactions.pop(0)
            elif points_to_spend <= remaining_points and payer_balance <= points_to_spend:
                remaining_points -= payer_balance
                spent -= payer_balance
                self.transactions.pop(0)
            elif points_to_spend < 0:
                spent -= points_to_spend
                self.transactions.pop(0)
            else:
                spent -= remaining_points
                payment['points'] -= remaining_points
                remaining_points = 0
            if payer in result:
                result[payer] += spent
            else:
                result[payer] = spent
            balances[payer] += spent
        return [{'payer': key, 'points': result[key]} for key in result]

    def _update_balance(self, payer, points):
        if payer in self.balances:
            self.balances[payer] += points
        else:
            self.balances[payer] = points
