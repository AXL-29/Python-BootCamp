import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
    "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?", "|", "\\", "~", "`"
]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters do you like in your passwords?: "))
nr_symbols = int(input("How many symbols would you like?: "))
nr_numbers = int(input("How many numbers would you like?: "))

password = []

# Add random letters
for i in range(nr_letters):
    password.append(random.choice(letters))

# Add random symbols
for i in range(nr_symbols):
    password.append(random.choice(symbols))

# Add random numbers
for i in range(nr_numbers):
    password.append(random.choice(numbers))

print(f"Unshuffled password list: {password}")

# Shuffle manually using a loop
for i in range(len(password)):
    j = random.randint(0, len(password)-1)
    password[i], password[j] = password[j], password[i]

# Convert list to string
password = "".join(password)

print(f"Your password is: {password}")
