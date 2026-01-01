import random
import pandas
import smtplib
from datetime import datetime

APP_PASSWORD = "password"
EMAIL = "gimpaojade4@gmail.com"

RANDOM_LETTER = random.choice([
    "letter_1.txt",
    "letter_2.txt",
    "letter_3.txt"
])

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {
    (row.month, row.day): row
    for (_, row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    name = birthday_person["name"]
    recipient_email = birthday_person["email"]

    with open(f"letter_templates/{RANDOM_LETTER}") as file:
        content = file.read()
        personalized_letter = content.replace("[NAME]", name).strip()

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=recipient_email,
            msg=f"Subject: Happy Birthday\n\n{personalized_letter}"
        )