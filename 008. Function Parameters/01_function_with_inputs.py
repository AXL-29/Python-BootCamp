# function - is a reusable code of block that does a specific job.

# syntax:
# def function_name(parameters):
#   code to run
#   return result

# def - keyword that tells Python you're defining a function.
# function_name - whatever name you choose (follow naming rules)
# parameters - data the function needs(can be empty)
# return - send a value back (optional)

name = input("What is your name: ")

def greet(name):
    print(f"Hi {name}")
    print(f"How do you do {name}")
    print(f"Goodbye {name}")

greet(name)