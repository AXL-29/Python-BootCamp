# Concepts: print(), input(), variables, string operations, f-strings, basic conversions.
# Task: Create a little onboarding flow for a fictional app.
# It should:
# It should:

# Ask the user for:
    # Their first name
    # Their age
    # Their favorite hobby

# Print:
# A welcome message using their name.
# How old they’ll be in 5 years.
# A short personalized line like:
# “Nice, [hobby] sounds fun! We’ll help you find more time for that.”

# Rules:
# Use at least two different ways to combine strings and variables (e.g., concatenation and f-strings).
# Make sure you convert types when needed (e.g., age input to number for math).

# TODO 1: Ask the user for their first_name, age, and favorite_hobby:
first_name = input("What is your first name?: ")
age = int(input("How old are you?: "))
favorite_hobby = input("What is your favourite hobby?: ")

# TODO 2: A welcome message using their name.
print("Greetings, " + first_name + " welcome to the dev world!")

# TODO 3: How old they'll be in 5 years
future_age = age + 5
print(f"You'll be {future_age} years old in 5 years")

# TODO 4: A short personalized line:
print(f"Nice, {favorite_hobby} sounds fun! We’ll help you find more time for that.")
