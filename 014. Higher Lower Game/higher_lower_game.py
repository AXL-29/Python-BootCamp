import art
from game_data import data
import random

print(art.logo)

for _ in range(len(data)):
    compare_a = random.choice(data)
    print(compare_a)
