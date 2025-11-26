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

# 5. Check if user is correct
def check_answer(user_guess, a_followers, b_followers):
    """Return True if the user's guess is correct, False if wrong."""

    # 5.2 Use if statement to check if user is correct.
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# 1. Display Art
print(logo)
score = 0
is_game_over = False

# 8. Make the game repeatable.
while not is_game_over:
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

    # 4. Ask user for a guess, make sure `guess` is guaranteed to be either "a" or "b"
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess in ["a", "b"]:
            break
        else:
            print("Invalid input! Please choose between 'A' and 'B' only. Thank you!")


    # 5.1 Get the follower count of each account
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    is_correct = check_answer(guess, follower_count_a, follower_count_b)

    # 6. Give user feedback on their guess
    # 7. Score Keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        is_game_over = True
# 9. Making account at position B become the next account at position A.
