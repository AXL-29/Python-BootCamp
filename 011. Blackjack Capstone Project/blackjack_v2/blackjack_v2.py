import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(player_score, computer_score):
    if player_score == 21 and computer_score != 21:
        return "You Win! Blackjack!"
    elif player_score != 21 and computer_score == 21:
        return "You Lose! Computer Blackjack!"
    else:
        return None   # no blackjack

def win_or_loss(player_score, computer_score):
    if player_score > 21:
        return "You Lose! Busted!"
    elif computer_score > 21:
        return "Computer Lose! Busted!"
    elif player_score > computer_score:
        return "You Win!"
    elif computer_score > player_score:
        return "You Lose!"
    else:
        return "It's a draw!"


def game():
    should_continue = True

    while should_continue:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

        if play == "y":
            player_cards = []
            computer_cards = []

            # initial deal
            for _ in range(2):
                player_cards.append(random.choice(cards))
            player_score = sum(player_cards)

            for _ in range(2):
                computer_cards.append(random.choice(cards))
            computer_score = sum(computer_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # check for blackjack immediately
            bj_result = blackjack(player_score, computer_score)
            if bj_result:
                print(bj_result)
                continue   # go back to "Do you want to play..." for a new round

            valid = True

            while valid:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if another_card == "y":
                    new_card = random.choice(cards)
                    player_cards.append(new_card)
                    player_score += new_card

                    print(f"Your cards: {player_cards}, current score: {player_score}")

                    # computer draw logic
                    if computer_score <= 12:
                        print("Computer cards are below or equal to 12, drawing another card...")
                        new_card = random.choice(cards)
                        computer_cards.append(new_card)
                        computer_score += new_card

                    print(f"Computer's cards: {computer_cards}, total score: {computer_score}")

                    # check result
                    result = win_or_loss(player_score, computer_score)
                    if result != "It's a draw!":
                        print(result)
                        valid = False  # end this round

                elif another_card == "n":
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Computer's cards: {computer_cards}, total score: {computer_score}")

                    result = win_or_loss(player_score, computer_score)
                    print(result)
                    valid = False  # exit loop

                else:
                    print("Invalid choice! Please try again!")

        else:
            should_continue = False
            print("Thanks for playing! Goodbye!!!")


game()
