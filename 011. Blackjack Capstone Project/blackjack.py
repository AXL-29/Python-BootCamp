import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True

while should_continue:

    # TODO-1: Create a user input that ask "Do you want to play a game of Blackjack? Type 'y' or 'n'"
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    # TODO-2: Conditional statement if 'y' continue, else end the game.
    player_card = []
    computer_card = []

    if play == 'y':
        # TODO-3: Display your cards, and computer's first card
        for card in range(2):
            card = random.choice(cards)
            player_card.append(card)
            player_score = sum(player_card)
        print(f"Your cards are {player_card}, current score: {player_score}")

        for card in range(2):
            card = random.choice(cards)
            computer_card.append(card)
        print(f"Computer first card is {computer_card[0]}")

        #TODO-4: Prompt if the player want to draw another card.
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_card == "y":
            last_card = random.choice(cards)
            player_card.append(last_card)
            player_score = sum(player_card)
            computer_score = sum(computer_card)
        print(f"Your cards are {player_card}, current score: {player_score}")
        print(f"Computer first card is {computer_card[0]}")
        print(f"Computer final card is {computer_card[1]}")

        # final scores:
        print(f"Your final score is {player_score}")
        print(f"Computer final score: {computer_score}")


    else:
        should_continue = False
        # end of game