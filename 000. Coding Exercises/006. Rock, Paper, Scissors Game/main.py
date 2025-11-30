# Task 6 – Rock, Paper, Scissors Game
# Goal: Create a Rock, Paper, Scissors game where:
    # The user plays against the computer.
    # The computer chooses randomly
    # You use conditionals, loops, and at least one function

# Requirements
# Ask the user to choose:
    # "rock", "paper", or "scissors"
# Have the computer randomly choose one of the three options too.
# Decide the winner:
    # Rock beats Scissors.
    # Scissors beats Paper.
    # Paper beats Rock
    # Same choice → draw

# Print the result, something like:
    # You chose rock, computer chose scissors – You win!
    # You chose paper, computer chose paper – It's a draw!
    # etc.

# Loop the game:
# After each round, ask:
    # "Do you want to play again? (yes/no):"
# If the user types "yes", start another round.
# If "no", exit the game with a goodbye message.

import random

choices = ["rock", "paper", "scissors"]

def win_or_loss(user_pick, computer_pick):
    if user_pick == computer_pick:
        return f"You chose {user_pick}, computer chose {computer_pick}. It's a draw!"
    elif (
        (user_pick == "rock" and computer_pick == "scissors") or
        (user_pick == "paper" and computer_pick == "rock") or
        (user_pick == "scissors" and computer_pick == "paper")
    ):
        return f"You chose {user_pick}, computer chose {computer_pick}. You Win!"
    else:
        return f"You chose {user_pick}, computer chose {computer_pick}. You Lose!"

while True:
    # Get valid user input
    user_choice = input("Please choose 'rock', 'paper', or 'scissors': ").lower()
    if user_choice not in choices:
        print("Invalid input! Please try again!")
        continue   # go back to the top of the loop

    # Computer picks
    computer_choice = random.choice(choices)

    # Show result
    print(win_or_loss(user_choice, computer_choice))

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == "yes":
            break  # go back to the main game loop for another round
        elif play_again == "no":
            print("Thanks for playing!")
            exit()  # or set a flag / break outer loop
        else:
            print("Please type 'yes' or 'no' only. Try again!")