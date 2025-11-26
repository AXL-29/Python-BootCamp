# Emoji Dice Roller (Days 4–5)
# Concepts: random, lists, indexing, basic branching.

# Task: Simulate a dice-rolling mini game using emojis.

# Create a set of 6 “dice faces” (like 🎲1, 🎲2, etc.).
# Ask the user how many dice they want to roll (1–5).
# Roll that many dice randomly.
# Show the individual results and the total.

# Rules:
    # If the user asks for more than allowed (greater than 5 or less than 1), show an error.
    # Each “face” should correspond to a value 1–6.

import random

# TODO 1: Create a set of 6 “dice faces” (like 🎲1, 🎲2, etc.).
dice_value = [1, 2, 3, 4, 5, 6]
dice_faces = ["🎲 1", "🎲 2", "🎲 3", "🎲 4", "🎲 5", "🎲 6"]

# TODO 2: Ask the user how many dice they want to roll (1–5).
valid= False
while not valid:
    try:
        number_of_dice = int(input("How many dice would you like to roll (1-5)?: "))
        if number_of_dice > 5 or number_of_dice < 1:
            print("Invalid input! Please choose between 1 and 5!")
        else:
            valid = True
    except ValueError as err:
        print(f"Error: {err}, please try again!")

# TODO 3: Roll that many dice randomly.
rolled_dice = []
for _ in range(number_of_dice):
        rolled_dice.append(random.choice(dice_value))
    
# TODO 4: Show the individual results and the total.
rolled_dice_faces = []
for dice in rolled_dice:
    rolled_dice_faces.append(dice_faces[dice - 1])

rolled_dice_faces = " ".join(rolled_dice_faces)
total = sum(rolled_dice)

print(f"Rolled dice: {rolled_dice_faces}")
print(f"The sum of dice: {total}")