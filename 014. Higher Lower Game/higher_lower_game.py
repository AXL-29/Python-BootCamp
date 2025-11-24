import art
from game_data import data
import random


print(art.logo)

random_account_a = random.choice(data)
print(f"Compare A: {random_account_a['name']}, {random_account_a['description']}, {random_account_a['country']}.")

print(art.vs)

random_account_b = random.choice(data)
print(f"Compare B: {random_account_b['name']}, {random_account_b['description']}, {random_account_b['country']}.")

user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

if user_choice == 'A':

