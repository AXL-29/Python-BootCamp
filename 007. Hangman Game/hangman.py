import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1:   Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
placeholder = ""
for char in chosen_word:
    placeholder += "_ "

print(placeholder)

# TODO-2:   Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

display = " a"
# TODO-3: Check if the letter the user (guess) is one to letters in the chosen_word. Print "right" if it is, "wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += " _ "
print(display)