# Debugging Leap Year:

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# Answer:

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))
print(is_leap(2020))
print(is_leap(1900))
print(is_leap(2021))

# The bug was in the third nested if condition: it incorrectly used 4000 instead of 400. Changing it to 400 ensures correct leap year calculation according to the standard rules.
