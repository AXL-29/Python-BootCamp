import art
from game_data import data
import random

print(art.logo)

# Pick account A
random_account_a = random.choice(data)
print(f"Compare A: {random_account_a['name']}, {random_account_a['description']}, {random_account_a['country']}.")

print(art.vs)

# Pick account B and make sure it's not the same as A
random_account_b = random.choice(data)
while random_account_b == random_account_a:
    random_account_b = random.choice(data)

print(f"Compare B: {random_account_b['name']}, {random_account_b['description']}, {random_account_b['country']}.")


def user_pick(option_a, option_b):
    """Return (user_account, computer_account) based on A/B input."""
    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if user_choice == "A":
            user = option_a
            computer = option_b
            return user, computer
        elif user_choice == "B":
            user = option_b
            computer = option_a
            return user, computer
        else:
            print("Invalid choice, please try again!")


# Now pass the FULL accounts, not just follower_count
user_choose, computer_choice = user_pick(random_account_a, random_account_b)

print(f"\nYou picked: {user_choose['name']} with {user_choose['follower_count']}M followers")
print(f"Computer gets: {computer_choice['name']} with {computer_choice['follower_count']}M followers")


if user_choose["follower_count"] > computer_choice["follower_count"]:
    print("You’re right! 🎉")
else:
    print("Sorry, that’s wrong 😔")
