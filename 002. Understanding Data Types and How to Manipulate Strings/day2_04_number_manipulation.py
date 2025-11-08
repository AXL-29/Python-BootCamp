weight = int((input("Enter your weight: ")))
height = float((input("Enter your height: ")))

bmi = weight / (height ** 2)

# Flooring a Number  - you can floor a number or remove all decimal places using the int() function.
# Which converts a floating point number (with deciimal places) into an integer (whole number).

print(int(bmi))

# Rounding a number - you can round a number using the round() functions to specified number of decimal places.
# Syntax: round(number, ndigits)

print(round(bmi, 2))

# Compound Assignment Operators  - An assignment operator is used to assign a value to a varAn assignment operator is used to assign a value to a variable.
# It tells Python to store a value on the right-hand side (RHS) into the variable on the left-hand side (LHS).
# Example of Compound Assignment Operators:
# +=    (add and assign)
# -=    (subtract and assign)
# *=    (multiple and assign)
# /=    (divide and assign)
# //=   (floor divide and assign)
# %=    (modulus and assign)
# **=   (exponentiate and assign)

a = 100
a += 10
print(a)

b = 100
b -= 50
print(b)

c = 100
c *= 2
print(c)

d = 100
d /= 4
print(d)

e = 100
e //= 3
print(e)

f = 100
f %= 7
print(f)

g = 100
g ** 2
print(g)

# f string (short for formatted string literal) lets you insert variables or expressions directly inside a string.
# Making it easier and cleaner to build dynamic messages.

name = "Jade Mark"
age = 25
height = 1.72
weight = 67

print(f"My name is {name}, {age} years old with a {height}m height and {weight}kg of weight.")