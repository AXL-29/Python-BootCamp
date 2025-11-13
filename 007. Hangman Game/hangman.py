import random

word_list = ["apple", "banana", "mango"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for i in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter: ")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
                
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")