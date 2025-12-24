# Advanced Python Arguments
# Arguments with a default value is a function parameter that already has a value,
# so the function can be called with or without passing that argument.

# Basic Idea:
# If the caller doesn't provide a value -> Python uses the default.
# If the caller does provide a value -> Python uses the new value.

def add(a, b=2, c=3):
    return (a, b, c)

print(add(1))
print(add(2, 2, 2))

# Why default arguments are useful?
# They help you:
    # Make functions optional & flexible.
    # Reduce repeated code.
    # Create a cleaner function calls
    # Match how Tkinter widgets works.

# Important Rule:
# Default arguments must come AFTER non-default arguments.
# wrong:

# def minus(a=10, b):
#     pass

# correct
def multiply(a, b=10):
    pass