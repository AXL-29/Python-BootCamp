import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)  # for testing

# Create placeholders for each letter
display = ["_"] * len(chosen_word)
print("".join(display))

while "_" in display:
    guess = input("Guess a letter: ").lower()

    # Update display if the guess is correct
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    print("".join(display))

print("You guessed the word!")
