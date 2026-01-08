import os
import requests
import urllib3
from twilio.rest import Client
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings (use only for testing / learning)
urllib3.disable_warnings(InsecureRequestWarning)

# -------------------- CONSTANTS -------------------- #
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = os.getenv("OWM_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")

LATITUDE = 14.477140
LONGITUDE = 120.892242

# -------------------- VALIDATION -------------------- #
if not all([
    API_KEY,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
    TWILIO_TO_NUMBER
]):
    raise ValueError("Missing required environment variables.")

# -------------------- TWILIO CLIENT -------------------- #
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# -------------------- WEATHER REQUEST -------------------- #
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    url=OWM_ENDPOINT,
    params=parameters,
    verify=False
)
response.raise_for_status()
data = response.json()

# -------------------- RAIN CHECK -------------------- #
will_rain = False

for forecast in data.get("list", []):
    weather = forecast.get("weather", [])
    if weather:
        weather_id = weather[0].get("id", 800)
        if weather_id < 700:
            will_rain = True
            break

# -------------------- SMS ALERT -------------------- #
if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=TWILIO_FROM_NUMBER,
        to=TWILIO_TO_NUMBER
    )
    print("SMS sent:", message.sid)
else:
    print("No rain expected. No SMS sent.")
