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

for i in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for j in range(1, nr_numbers + 1):
    password.append(random.choice(symbols))

for k in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

print(password)

random.shuffle(password)
print(password)

password = "".join(password)

print(f"Your password is: {password}")