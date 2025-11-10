# list - is a collection of items (like numbers, words, or other objects) stoted in a single variable.
#        it's like a container that holds multiple values, usually in square brackets[], separated bt commas.

# example:
fruits = ["apple", "banana", "mango", "orange"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hello", 10, True, 3.14]

# Key Features:
# - List can hold different data types (strings, integers, booleans and etc.)
# - List are ordered (each item has an index starting from 0)
# - List are mutable, meaning you can change, add or remove items after creation

# Accessing List items:
print(fruits[2])    # banana
print(fruits[-1])   # orange

# changing an item in a list.
fruits[0] = "strawberry"
print(fruits[0])

# adding an item in a list:
fruits.append("kiwi")
print(fruits)

# adding multiple items in a list:
fruits.extend(["guava", "pear", "watermelon"])
print(fruits)