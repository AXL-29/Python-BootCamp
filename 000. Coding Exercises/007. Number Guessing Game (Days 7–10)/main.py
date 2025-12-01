# Number Guessing Game (Days 7–10)
# Concepts: while loop, conditionals, comparison, functions, difficulty setting.
# Task:
# Create a guess the number game:

# Program selects a random number within a range.
    # Ask player to choose difficulty:
    # Easy = more attempts - done
    # Hard = fewer attempts - done

# On each guess:
    # Tell them “Too high”, “Too low”, or “Correct!” - done
    # Reduce remaining attempts - done

# End when:
    # They guess correctly - done
    # Or they run out of attempts - done

# Rules:
    # Use at least one function for generating the number or running the main loop.
    # Show remaining attempts after each wrong guess.

import random  # Import random module to generate the number to guess

# Number to be guessed. 
def difficulty():
    """Prompt the user to choose a difficulty level and return the corresponding number of attempts."""
    while True:
        level = input("Choose your difficulty level – 'easy' (10 attempts) or 'hard' (5 attempts): ").lower()
        if level == "easy":
            print("Easy mode selected! You have 10 attempts to guess the number.")  # Friendly confirmation
            return 10
        elif level == "hard":
            print("Hard mode selected! You have 5 attempts to guess the number.")  # Friendly confirmation
            return 5
        else:
            print(f"Oops! '{level}' is not valid. Please type 'hard' or 'easy' only.")  # Clear error message

def check_guess(number_to_guess, remaining_attempts):
    """Take the user's guess, compare it to the target number, indicate if it is too high, too low, or correct, and reduce the remaining attempts."""
    while True:
        print(f"\nYou have {remaining_attempts} attempt(s) left.")  # Clear display of remaining attempts
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            
            # Validate the guess is within allowed range
            if user_guess < 1 or user_guess > 100:
                print("Your guess must be a number between 1 and 100. Try again!")
            elif user_guess > number_to_guess:
                remaining_attempts -= 1
                print("Too high! Aim lower.")
            elif user_guess < number_to_guess:
                remaining_attempts -= 1
                print("Too low! Try a higher number.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
                break  # Exit loop since user guessed correctly
            
            # Check if user has run out of attempts
            if remaining_attempts == 0:
                print(f"\n😢 You've run out of attempts. The number was: {number_to_guess}")
                print("Better luck next time!")
                break

        except ValueError as e:
            print(f"Invalid input! Please enter a whole number. ({e})")

def number_guessing_game():
    """Main game loop that handles new rounds and play-again option."""
    number_to_guess = random.randint(1, 100)  # Generate first random number
    check_guess(number_to_guess, remaining_attempts=difficulty())  # Start first round
    while True:
        play_again = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
        if play_again == "yes":
            number_to_guess = random.randint(1, 100)  # Generate new number for new game
            check_guess(number_to_guess, remaining_attempts=difficulty())  # Start new round
        elif play_again == "no":
            print("\nThank you for playing! See you next time! 👋")
            break
        else:
            print("Please type 'yes' or 'no' only. Try again.")

number_guessing_game()  # Start the game
