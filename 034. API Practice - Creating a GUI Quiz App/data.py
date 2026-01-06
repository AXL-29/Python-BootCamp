import requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://opentdb.com/api.php"
AMOUNT = 10
TYPE = "boolean"

params = {
    "amount": AMOUNT,
    "type": TYPE,
    "category": 18,
}

response = requests.get(url=URL, params=params, verify=False)
response.raise_for_status()

question_data = response.json()["results"]