# SMTP (Simple Mail Transfer Protocol) - is the standard protocol used to send emails from a client
# (your app or email client) to a mail server, and between mail servers.

# smtplib - is a built-in Python library taht lets your Python program send emails using SMTP.

import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login("gimpaojade4@gmail.com", "lhlx yniz kiix ohhr")
    connection.sendmail(
        from_addr="gimpaojade4@gmail.com",
        to_addrs="gimpao22@gmail.com",
        msg="""
            Subject: Test

            Hello from Python!
            """
    )