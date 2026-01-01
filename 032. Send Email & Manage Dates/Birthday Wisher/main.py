from datetime import datetime
import random
import pandas

today = datetime.now()
today_month = today.month
today_day = today.day

data = pandas.read_csv("birthdays.csv").to_dict(orient="records")

for person in data:
    if person["month"] == today_month and person["day"] == today_day:

        letter_file = random.choice([
            "letter_1.txt",
            "letter_2.txt",
            "letter_3.txt"
        ])

        with open(f"letter_templates/{letter_file}") as file:
            letter = file.read()
            personalized_letter = letter.replace("[NAME]", person["name"])

        print(personalized_letter)  # test output first
