import random
from game_data import data
from art import logo, vs

# 3. Format the account data into printable data
def format_data(account):
    """Format the account data into printable data"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from{account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    a_followers = 0
    b_followers = 0

    while True:
        if user_guess == "a":
            a_followers = account_a["follower_count"]
        elif user_guess == "b":
            b_followers = account_b["follower_count"]
        else:
            print("Invalid input! Please choose between 'A' and 'B' only. Thank you!")



# 1. Display Art
print(logo)

# 2. Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)

# 2.1 Re-generate account_b if equal to account_a
if account_b == account_a:
    account_b = random.choice(data)

# 3.1 Print the account data
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

# 4. Ask user for a guess.
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# 5. Check if user is correct
    # 5.1 Get the follower count of each account
follower_count_a = account_a["follower_count"]
follower_count_b = account_a["follower_count"]

check_answer(guess, follower_count_a, follower_count_b)

    # 5.2 Use if statement to check if user is correct.
# 6. Give user feedback
# 7. Score Keeping
# 8. Make the game repeatable.
# 9. Making account at position B become the next account at position A.
