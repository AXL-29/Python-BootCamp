# Indentation in Python
# ====================
# Python uses indentation (whitespace at the beginning of lines) to define code blocks.
# Indentation is mandatory and defines the scope of loops, functions, classes, and conditionals.
# Consistent indentation is critical - mixing spaces and tabs will cause errors.

# Example 1: Function definition
def greet(name):
    # This line is indented - it's inside the function
    print(f"Hello, {name}!")
    return name

greet("Alice")

# Example 2: If statement
age = 20
if age >= 18:
    # This block is indented - executes if condition is True
    print("You are an adult")
else:
    # This block is indented - executes if condition is False
    print("You are a minor")

# Example 3: For loop
for i in range(3):
    # This block is indented - executes for each iteration
    print(f"Count: {i}")

# Example 4: Nested indentation
for i in range(2):
    if i == 0:
        # Double indentation for nested blocks
        print("First iteration")
    else:
        print("Second iteration")

# Example 5: Class definition
class Dog:
    def __init__(self, name):
        # Indented method body
        self.name = name
    
    def bark(self):
        # Indented method body
        print(f"{self.name} says: Woof!")

dog = Dog("Rex")
dog.bark()