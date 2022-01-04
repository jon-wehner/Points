# Points
A web service that accepts HTTP requests to keep track of user balances.

## Installation (Running the service)
This is the most basic method for installing the project dependencies and running the service. You may wish to run the application in an isolated environment. In that case, you should follow the development installation instructions. 
1. Ensure python 3.6 or newer is installed on your system.
- For assistance installing python on your operating system please see: https://wiki.python.org/moin/BeginnersGuide/Download
3. Clone the repo
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
5. Make requests to the app.
- Use any application that allows you to make http requests containing JSON to use the application. JSON formatting is provided in the API routes section to assist you when formatting your requests.
- An example transaction request using cURL:
```
curl -X POST 127.0.0.1:5000/transaction -H 'Content-Type: application/json' -d '{"payer":"DANNON", "points":"5000","timestamp":"2020-11-02T14:00:00Z"}'
```
## Installation (Development)
Instruction may vary depending on virtual environment solution, this project was developed with pipenv. 
1. Ensure python 3.9 and pipenv are installed on your system
- For assistance installing python on your operating system please see: https://wiki.python.org/moin/BeginnersGuide/Download
- For assistance installing pipenv please see: https://pipenv.pypa.io/en/latest/install/#installing-pipenv
3. Clone the repo
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
- The service will run at 127.0.0.1:5000
5. Make requests to the app.
- Use any application that allows you to make http requests containing JSON to use the application. JSON formatting is provided in the API routes section to assist you when formatting your requests.
- An example transaction request using cURL:
```
curl -X POST 127.0.0.1:5000/transaction -H 'Content-Type: application/json' -d '{"payer":"DANNON", "points":5000,"timestamp":"2020-11-02T14:00:00Z"}'
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
Points is an integer value representing total points to spend.

This route returns a JSON array with objects for every payer that had points spent and the amount of points spent. The JSON will have the following format:
```
[
{"payer": payer, "points": points}
]
```
Payer will be a string value with the payer name
Points is an integer value for the points spent from that payer balance.

## Documentation Sources Used
1. Python Docs: https://docs.python.org/3.9/
2. Flask Docs: https://flask.palletsprojects.com/en/2.0.x/
3. Pytest Docs: https://docs.pytest.org/en/6.2.x/contents.html
