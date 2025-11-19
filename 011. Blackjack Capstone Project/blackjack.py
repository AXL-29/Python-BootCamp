import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True

while should_continue:

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play == 'y':
        player_cards = []
        computer_cards = []

        # Deal 2 cards to player
        for _ in range(2):
            player_cards.append(random.choice(cards))
        player_score = sum(player_cards)

        # Deal 2 cards to computer
        for _ in range(2):
            computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Ask if player wants another card
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if draw_card == "y":
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)

        # After the draw decision, show final hands and scores
        print("\n--- Final Results ---")
        print(f"Your final cards: {player_cards}, final score: {player_score}")
        print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")

        # Decide the winner
        if player_score > 21 and computer_score > 21:
            print("Both went over 21. It's a draw!")
        elif player_score > 21:
            print("You went over 21. You lose! 😭")
        elif computer_score > 21:
            print("Computer went over 21. You win! 😁")
        elif player_score > computer_score:
            print("You win! 😁")
        elif player_score < computer_score:
            print("You lose! 😤")
        else:
            print("It's a draw! 🙃")

        print()  # blank line for spacing

    else:
        should_continue = False
        print("Game ended. Thanks for playing! 👋")
