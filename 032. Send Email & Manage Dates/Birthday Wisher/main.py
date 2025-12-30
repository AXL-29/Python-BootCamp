import smtplib

EMAIL = "gimpaojade4@gmail.com"
APP_PASSWORD = "lhlx yniz kiix ohhr"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(EMAIL, APP_PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="gimpao22@gmail.com",
        msg="""Subject: Test

            Hello from Python!
            """
    )
