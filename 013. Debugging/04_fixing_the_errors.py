# 4. Fix the Errors:
# Fix any errors (red underlines) that appear in the editor before running the code.
# Warnings (yellow) are optional fixes; sometimes they may cause problems later,
# but other times the editor just doesn't fully understand your code.

age = int(input("How old are you?: "))
# This line can raise an error if the user types a non-integer value.

if age > 18:
    print("You can drive at age {age}")
# This will also cause a bug because the age is not displayed correctly;
# it is not inside an f-string.

# ValueError: Invalid literal for int() with base 10:
# This error occurs when the string provided to int() cannot be parsed as an integer.

# You can handle this kind of error using a try/except block.
age = None
while age is None:
    try: 
        age = int(input("How old are you?: "))
    except ValueError:
        print("You have typed an invalid input! Please try again!")

    if age > 18:
        print("You can drive at age {age}")

if age > 18:
    print(f"You can drive at {age}")
else:
    print(f"You are too young to drive at age {age}")

# To properly handle errors with age input, we can use a while loop to keep asking
# until the user enters a valid value.
# Also, adding an else statement ensures all input values are properly handled.
