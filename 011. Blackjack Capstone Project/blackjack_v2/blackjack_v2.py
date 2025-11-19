import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True

while should_continue:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play == "y":
        player_cards = []
        computer_cards = []
        player_score = 0
        computer_score = 0

        for _ in range(2):
            player_cards.append(random.choice(cards))
        player_score += sum(player_cards)
            
        for _ in range(2):
            computer_cards.append(random.choice(cards))
        computer_score += sum(computer_cards)

        if computer_score < 12:
            computer_cards.append(random.choice(cards))
            computer_score += sum(computer_cards)
        
        print(computer_cards)
        print(computer_score)
    else:
        should_continue = False
        print(f"Thanks for playing! Goodbye!!!")
