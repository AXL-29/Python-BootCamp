# Higher Order Functions:
# A higher-order function is a function that does at least one of these:
    # 1. Takes another function as an argument
    # 2. Returns a function
# In short: Functions that work with other functions


# Example1: Function as an argument

def greet(name):
    return f"Hello, {name}"

def process(func, value):
    return func(value)

print(process(greet, "Jade"))

# What's happening:
    # 'greet' is passed without parentheses
    # 'process' calls it using 'func(value)'

# Example2: Function that returns another function
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
print(double(5))

# Explanation:
    # 'multiplier(2)' returns 'multiply'
    # "double' becomes a function

# Common Built-in Higher-Order Functions
# map()         - Apply functions to all items
# filter()      - Keep items that match a condition
# sorted()      - Sort using a function
# reduce()      - Combine values (from 'functools')

# Example:
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))

print(squared)


# Event Listeners (Event Handlers) in Python
# An 'event listener' is a function that waits for something to happen, like:
    # A button click
    # A key press
    # A mouse movement
    # A timer finishing

    # Common in GUI, games, and web apps


