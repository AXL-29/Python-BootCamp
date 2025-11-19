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

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        valid = True

        while valid:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if another_card == "y":
                new_card = random.choice(cards)
                player_cards.append(new_card)
                player_score += new_card   # no need for int() if cards are already ints

                # show updated hand if you want
                print(f"Your cards: {player_cards}, current score: {player_score}")

                if computer_score <= 12:
                    print("Computer cards are below 12, drawing another card...")
                    new_card = random.choice(cards)
                    computer_cards.append(new_card)
                    computer_score += new_card

                print(f"Computer's cards: {computer_cards}, total score: {computer_score}")


                    # you probably DON'T want to stop here yet,
                    # so don't set valid = False unless this is intentional

            elif another_card == "n":
                print(f"Your final cards: {player_cards}, final score: {player_score}")
                print(f"Computer's cards: {computer_cards}, total score: {computer_score}")
                valid = False  # exit loop

            else:
                print("Invalid choice! Please try again!")
                # no need to change `valid`; it stays True

        
        
    else:
        should_continue = False
        print(f"Thanks for playing! Goodbye!!!")
