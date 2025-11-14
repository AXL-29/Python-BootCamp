import random
from hangman_art import hangman_logo
from hangman_words import word_list

stages = [
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

print(hangman_logo)

chosen_word = random.choice(word_list)

placeholder = ""

for i in chosen_word:
    placeholder += "_"

print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"You have {lives} lives left.")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guess {guess}")
        print(stages[lives])
        continue

    display = " "

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You Lose.")
    else:
        print(f"Good job! {guess} is in the word.")
        print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You Win!")