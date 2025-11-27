# Random Lunch Picker (Days 4–6)
# Concepts: lists, random selection, while loop, simple menu.

# Task: Help a user pick what to eat for lunch.
# Start with a predefined list of lunch options.
# Show a mini menu:
    # Add a new option
    # Show all options
    # Pick a random lunch
    # Remove an option
    # Exit
    # Loop until the user chooses to exit.

# Rules:
# Handle the case where the list is empty when picking random lunch.
# Let the user remove by name; handle non-existent names gracefully.

import random

# TODO 1: Create a list for menu
import random

# Predefined lunch options
menu = ["Burger", "Pizza", "Sushi", "Salad", "Pasta", "Tacos", "Sandwich"]

def show_menu(current_menu):
    """Display all lunch options in a numbered list."""
    if not current_menu:
        print("No options available.")
    else:
        print("Here's the available options for your lunch:")
        for i, option in enumerate(current_menu, 1):
            print(f"{i}. {option}")

def add_option(current_menu):
    """Add a new option to the menu."""
    new_option = input("What's the new option you want to add?: ").title()
    if new_option:  # Check if input is not empty
        current_menu.append(new_option)
        print(f"{new_option} has been added to the menu!")

def remove_option(current_menu):
    """Remove an option by name, handling non-existent names."""
    if not current_menu:
        print("Menu is empty. Nothing to remove.")
        return
    show_menu(current_menu)
    option_to_remove = input("Enter the option you want to remove: ").title()
    if option_to_remove in current_menu:
        current_menu.remove(option_to_remove)
        print(f"{option_to_remove} has been removed from the menu!")
    else:
        print(f"{option_to_remove} is not in the menu.")

def pick_random_lunch(current_menu):
    """Pick a random lunch option, handling empty menu."""
    if not current_menu:
        print("Menu is empty. Please add some options first.")
    else:
        print(f"Your random lunch for today is: {random.choice(current_menu)}")

def mini_menu():
    """Main loop for the lunch picker."""
    while True:
        print("\nMini Menu List:")
        print("1. Add a new option")
        print("2. Show all options")
        print("3. Pick a random lunch")
        print("4. Remove an option")
        print("5. Exit\n")
        try:
            choice = int(input("Please choose between 1 and 5: "))
            if choice == 1:
                add_option(menu)
            elif choice == 2:
                show_menu(menu)
            elif choice == 3:
                pick_random_lunch(menu)
            elif choice == 4:
                remove_option(menu)
            elif choice == 5:
                print("Thank you! Enjoy your lunch!")
                break
            else:
                print("Invalid input! Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")

# Start the lunch picker
mini_menu()