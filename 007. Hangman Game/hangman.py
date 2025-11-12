import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1:   Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

chosen_word = list(chosen_word)

# TODO-2:   Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_input = input("Guess a letter: ")

guess = []

# TODO-3: Check if the letter the user (guess) is one to letters in the chosen_word. Print "right" if it is, "wrong" if it's not.
for letter in chosen_word:
    if user_input.lower() == letter:
        print("right")
        guess.append(user_input)
    else:
        print("wrong")
        guess.append("_")

guess = " ".join(guess)
print(guess)

