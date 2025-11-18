def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(is_leap_year(1700))