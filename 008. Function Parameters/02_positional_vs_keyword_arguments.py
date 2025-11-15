# When a function needs more than one piece of data, you give it multiple parameters, separated by commas.

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# positional arguments - are arguments that are passed to a function based on their position (order), not their name.
# They match the parameters from left to right.
greet_with("Jade", "Canada") # positional arguments

# keyword arguments - are arguments that you pass to a function by explicitly naming the parameters, rather than relying on their position.
# This makes your code more readable and lets you pass arguments in any order.
greet_with(location="Canada", name="Jade")