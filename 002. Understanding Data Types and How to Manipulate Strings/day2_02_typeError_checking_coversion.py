# TypeError - These errors occur when you are using the wrong data type. e.g len(12345)
# Because you can only give the len() function a string, list, or tuple.

# len(12345)  This will raise a TypeError
# str() - use to convert other data types to String
print(len(str(12345)))

# type() function - use to check the data type of any value or variable in python.
print(type("12345"))
print(type(12345))
print(type(12.345))
print(type(True))

# ValueError: invalid literal for int() with base 10: 'abc'
# This happen when you try to convert a string into an integer using the int() function - but the string does not represent a valid number.

# print(int("abc") + int("123")) This will raise a ValueError

# Data types conversion

a = int("123") # convert data types into integer.
b = float("3.14159") # convert data type into float.
c = str(123) # convert data type into string
d = bool("False") # convert data type into boolean


print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Fix this line of code:
# print("Number of letters in your name: " + len(input("Enter your name: ")))

username = input("Enter your name: ")
length_of_name = len(username)
print("Number of letters in your name: " + str(length_of_name))