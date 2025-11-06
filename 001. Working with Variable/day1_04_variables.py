# variable - is like a container or a box that stores data 
#            such as a number, text, or any value — so you can 
#            use it later in your program.

name = input("What is your name: ")
print(name)

# you can also overwrite the value of the variable
name = input("What is your name: ")
print(name)

# Explanation:
# name = input("What is your name: ")
# This line asks the user for their name and stores it in the variable name.
# print(name)
# This displays whatever the user typed.
# Then you ask again with another input(), and because variables can change,
# the new value replaces (overwrites) the old one.


# len() - use to get the length of a string.
username = input("What is your name: ")
length = len(username)
print(length)