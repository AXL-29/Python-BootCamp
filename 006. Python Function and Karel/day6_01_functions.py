# In Python, a function - is a reusable block of code that performs a 
# specific task. Functions help organize code, make it more readable, 
# and allow you to avoid repetition.

# Key Features of Python Function:
# - Define using def keyword
# - Can take parameters (inputs)
# - Can return a value using the return statement.
# - Can be called multiple times in your program.

# Syntax on defining a function:
# def function_name(parameters):
#   code block
#   return result

name = input("Input your name: ")

def greet_user(name):
    return f"Hello, {name}"

print(greet_user(name))