# Raising an exception means you are intentionally triggering an error when something is wrong,
# instead of letting the program continue with bad or invalid data.

# Why raise an exception:
    # Validate user input
    # Prevent invalid program states
    # Make bugs easier to detect
    # Enforce rules inside functions

# Basic Syntax: raise ExceptionType("Error Message")

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

# If the user enters negative numbers, the program stops immediately and shows the error message.
