import smtplib
import time
import requests
from datetime import datetime
import urllib3

EMAIL = "gimpaojade4@gmail.com"
PASSWORD = "password"
MY_LAT = 12.879721
MY_LNG = 121.774017

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True

    return None


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=params,
        verify=False
    )
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True

    return None

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject: LOOK UP!\n\nThe ISS is above you!"
            )