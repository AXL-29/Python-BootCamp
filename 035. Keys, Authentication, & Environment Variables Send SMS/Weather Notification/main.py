import requests

API_KEY = "48289d3f3be5b573baf1f5c508beeca7"

parameter = {
    "q": "London,UK",
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameter)
print(response.json())

