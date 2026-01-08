import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "48289d3f3be5b573baf1f5c508beeca7"

parameter = {
    "lat": 14.477140,
    "lon": 120.892242,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=OWM_ENDPOINT, params=parameter)
response_code = response.status_code
data = response.json()

will_rain = False

for forecast in data.get("list", []):
    if forecast.get("weather"):
        weather_id =  forecast["weather"][0]["id"]

        if weather_id < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella!")