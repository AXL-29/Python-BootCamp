import art
from game_data import data
import random

def format_account(account):
    """Return a formatted string for an account."""
    return f"{account['name']}, {account['description']}, {account['country']}"

def user_pick(option_a, option_b):
    """Return (user_account, computer_account) based on A/B input."""
    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        if user_choice == "A":
            return option_a, option_b
        elif user_choice == "B":
            return option_b, option_a
        else:
            print("Invalid choice, please try again!")

def game_play():
    """Runs the main Higher-Lower game loop."""
    score = 0
    is_game_over = False

    # Pick initial accounts
    random_account_a = random.choice(data)
    random_account_b = random.choice(data)
    while random_account_b == random_account_a:
        random_account_b = random.choice(data)

    while not is_game_over:
        # Display game state
        print(art.logo)
        print(f"Current Score: {score}\n")
        print(f"Compare A: {format_account(random_account_a)}")
        print(art.vs)
        print(f"Compare B: {format_account(random_account_b)}")

        user_choose, computer_choice = user_pick(random_account_a, random_account_b)

        print(f"\nYou picked: {user_choose['name']} with {user_choose['follower_count']}M followers")

        if user_choose["follower_count"] > computer_choice["follower_count"]:
            print("You’re right! 🎉")
            score += 1
            # Winner stays as A for next round, pick a new B
            random_account_a = user_choose
            random_account_b = random.choice(data)
            while random_account_b == random_account_a:
                random_account_b = random.choice(data)
        else:
            print(f"Sorry, that’s wrong! Your final score: {score}")
            is_game_over = True

# Start the game
game_play()
