import random

rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
    """

paper = """
        _______
    ---'    ____)
            ______)
            _______)
            _______)
    ---.__________)
    """

scissors = """
        _____
    ---' ____)____
            ______)
         _________)
         (____)
   ---.__(___)
    """

rock_paper_sciscors = [rock, paper, scissors]

print("Welcome to Rock, Paper, Sciscor Game!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# computer oponent random choice.
computer_choice = random.randint(0, 2)

# user choice_ascii print
if user_choice == 0:
    print(f"You have chose: {rock_paper_sciscors[user_choice]}")
elif user_choice == 1:
    print(f"You have chose: {rock_paper_sciscors[user_choice]}")
elif user_choice == 2:
    print(f"You have chose: {rock_paper_sciscors[user_choice]}")
else:
    print("Please choice a valid range! Please try again!")

# computer_choice ascii print
if computer_choice == 0:
    print(f"Computer chose: {rock_paper_sciscors[computer_choice]}")
elif computer_choice == 1:
    print(f"Computer chose: {rock_paper_sciscors[computer_choice]}")
else:
    print(f"Computer chose: {rock_paper_sciscors[computer_choice]}")

# Winning or Lossing Condition:
if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2):
    print("You Lose!")
elif (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
    print("You Win!")
elif user_choice == computer_choice:
    print("Draw!")
else:
    print("Please choice a valid range! Please try again!") 