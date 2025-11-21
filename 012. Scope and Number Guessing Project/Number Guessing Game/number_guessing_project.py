# TODO 1: Import the method art and display the logo.
# TODO 2: Display a Welcome Message
# TODO 3: Generate random number from 1 - 100 and name it number_to_guess
# TODO 4: Let the user choose difficulty (easy = 5 attempts, hard = 10 attempts)
# TODO 5: Prompt a Make a guess
# TODO 6: Create a function of play() and

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# List of numbers and pick a random number from 1-100 to guess
list_of_numbers = []
for i in range(1, 101):
    list_of_numbers.append(i)
number_to_guess = random.choice(list_of_numbers)

# Allocated the numbers of attempt based on the difficulty:
attempts = 0
is_valid = False
while not is_valid:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 5
        is_valid = True
    elif difficulty == "hard":
        attempts = 10
        is_valid = True
    else:
        print("Invalid Choice! Please try again!")

print(f"You have {attempts} attempts remaining to guess the number.")


is_game_over = False
while not is_game_over:
    guess = int(input("Make a guess: "))
    for i in range(attempts):
        if guess != number_to_guess:
            attempts -= 1

        print(attempts)