# random() module is a built-in library that allows you to generate random numbers and make random selections.
# it's often used for things like:
# simulating random events
# creating test data
# shuffling items
# making games (like rolling dice  or picking random cards)


# Common Functions in the random module
# random()      -> returns a random float between 0.0 and 1.0                   -> random.random()                 -> 0.932
# randit(a, b)  -> returns random integer between a and b (inclusive)           -> random.randit(1, 10)            -> 8
# uniform(a, b) -> returns a random float between a and b                       -> random.uniform(1, 10)           -> 4.65
# choice(seq)   -> picks one random item from a list, tuple or string           -> random.choice(['a', 'b', 'c'])  -> 'a'
# shuffle(seq)  -> randomly reorders elements in a list(changes it in place)    -> random.shuffle(my_list)
# sample(seq, k)-> picks k unique random items from a list                      -> random.sample(range(1, 50) 6)   -> [1, 4, 5, 34, 23]

import random

random.randint(1, 6)
print(random)