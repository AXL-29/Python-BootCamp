# A docstring is a string at the start of a function, class, or module that explains what it does.

def is_leap_year(year):
    """
    Return True if the given year is a leap year, otherwise False.

    A leap year is:
    - divisible by 4
    - except if it's divisible by 100
    - unless it's also divisible by 400
    """
    # function code here
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(is_leap_year(2000))
print(is_leap_year(2001))