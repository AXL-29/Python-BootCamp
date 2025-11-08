# Primitive Data Types - (also known as basic data types) are the simplest kinds of data that form the building blocks for all other types. 
# They store single values and are not made up of other data types.

# 1. String (str) = Represents textual data — a sequence of characters enclosed in quotes (' ' or " ").
word = "String"
print("123" + "456") #concatenation

# 2. Integers (int) = Used to represent whole numbers — both positive and negative, without decimals.
number = 123
print(123 + 456)

# Large Integers dividers, use to visualize the large integers easily.
print(123_456_789_000)

# 3. Floating Number (float) = Used for decimal or real numbers.
decimal = 3.14159
print(decimal)
# 4. Boolean (bool) = Represents True or False values — often used in conditions or logic.
statement = True


# Subscripting - means accessing individual elements inside a sequence (like a string, list, or tuple) using square bracket[] and index number.
# It is called "subscriptig" because your asking python to give you the item at a specific position (or "subscript") in the sequence.

word = "Python"
print(word[0])
print(word[1])
print(word[-1]) # -1 use to get (last character)

# TypeError: Object of type 'int' has no len()
# This error means that you use the len() function on a value that's an integer (int), but integers don't have a "length".
# The len() function only works on sequences or collections - things that contains multiple items, like:
# str(strings), list, tuple, dict and set.