import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1:   Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2:   Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

display = []
# TODO-3: Check if the letter the user (guess) is one to letters in the chosen_word. Print "right" if it is, "wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("right")
        display.append(guess)
    else:
        print("wrong")
        display.append("_")
display = " ".join(display)
print(display)

