import requests

# parameters for the API
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

# API call
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
