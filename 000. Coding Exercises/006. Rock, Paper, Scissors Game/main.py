import random

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

def calculate_win(user_choose, computer_random_choice):
    if (user_choose == "rock" and computer_random_choice == "scissors") or (user_choose == "paper" and computer_random_choice == "rock") or (user_choose == "scissors" and computer_random_choice == "paper"):
        print(f"You choose {user_choose}, computer choose {computer_random_choice} - You Win!")
    elif (user_choose == "scissors" and computer_random_choice == "rock") or (user_choose == "rock" and computer_random_choice == "paper") or (user_choose == "paper" and computer_random_choice == "scissors"):
       print(f"You choose {user_choose}, computer choose {computer_random_choice} - You Lose!")
    else:
        print(f"You choose {user_choose}, computer choose {computer_random_choice} - It's a draw!")

choices = ["rock", "paper", "scissors"]

computer_choice = random.choices(choices)

while True:
    user_choice = input("Please choose 'rock', 'paper', 'scissors': ").lower()
    if user_choice not in choices:
        print("Invalid input! Please try again!")
    else:
        break

calculate_win(user_choice, computer_choice)