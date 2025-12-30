# datetime - is a built-in Python module used to work with dates and times
# such as getting the current date, current time or scheduling things.

# Why datetime is important:
    # Get the current date and time
    # Add or subtract days, hours, minutes
    # Timestamps logs, emails, or alerts
    # Schedule tasks (Like sending emails on specific days)

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1999, month=12, day=29)

print(date_of_birth)