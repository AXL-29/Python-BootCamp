import random
import art

def play():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:  # Main game loop for replay
        number_to_guess = random.randint(1, 100)

        # Choose difficulty
        while True:
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            if difficulty == "easy":
                attempts = 10
                break
            elif difficulty == "hard":
                attempts = 5
                break
            else:
                print("Invalid Choice! Please try again!")

        remaining_attempts = attempts

        # Guessing loop
        while remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if guess > number_to_guess:
                remaining_attempts -= 1
                print("Too high!")
            elif guess < number_to_guess:
                remaining_attempts -= 1
                print("Too low!")
            else:
                print("You got it! You win!")
                break  # Exit guessing loop

            if remaining_attempts == 0:
                print(f"You've run out of attempts! The number was {number_to_guess}.")

        # Ask to play again
        retry = input("Wanna play again? Type 'y' or 'n': ").lower()
        if retry != "y":
            print("Thank you for playing! Goodbye!")
            break  # Exit main game loop

play()
