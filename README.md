# Points
A web service that accepts HTTP requests to keep track of user balances.

## Installation (Running the service)
1. Ensure python 3.6 or newer is installed on your system. 
2. Clone the repo
  ```
  git clone https://github.com/jon-wehner/Points.git
  ```
3. Install dependencies
  ```
  pip install install -r requirements.txt
  ```
4. Run the service
  ```
  flask run
  ```
## Installation (Development)
Instruction may vary depending on virtual environment solution, this project was developed with pipenv. 
1. Ensure python 3.9 is installed on your system
2. 2. Clone the repo
  ```
  git clone https://github.com/jon-wehner/Points.git

  ```
3. Install dependencies
  ```
  pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
  ```
4. Run the service
  ```
  flask run
  ```
## API Routes
### GET /balances
Get requests to this route will return JSON containing all of the user balances with the following format:
```
{"payer": points}
```
### POST /transaction
Add a transaction to the user's account.

Post requests to this route accept JSON with the following format:
```
{"payer": payer, "points": points, "timestamp":timestamp}
```
payer is a string containing the payer name
points is an integer representing the points value of the transaction.
timestamp is a timestamp string in ISO 8061 with date and time(hour, min, seconds, tz optional). Note: At this time the app does not handle invalid date strings but error handling will be added in the future. 

If a valid transaction was submitted, the route will return a JSON with the following format:
```
{"Message": "Transaction successful"}
```

### POST /spend
Spend the user's points. This will spend the oldest points first and not allow the balance with any payer to go negative.

Post requests to this route accept JSON with the following format:
```
{"points": points}
```
Points is an integer value. 
