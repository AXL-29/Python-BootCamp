import smtplib, random
import datetime as dt

EMAIL = "gimpaojade4@gmail.com"
APP_PASSWORD = "password"

def random_quotes():
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)
    
    return quotes

def smtp_email(s_quote, email_subject=""):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="gimpao22@gmail.com",
            msg=f"""Subject: {email_subject}

                {s_quote}
                """
        )

now = dt.datetime.now()
weekday = now.weekday()

subject = "Motivational Quotes"
quote = random_quotes()

if weekday == 0:
    smtp_email(quote, subject)