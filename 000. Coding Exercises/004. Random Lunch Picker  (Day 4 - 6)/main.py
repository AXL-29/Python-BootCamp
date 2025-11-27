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
menu = ["Burger", "Pizza", "Sushi", "Salad", "Pasta", "Tacos", "Sandwich"]

def menu_option(current_menu):
    print("Here's the available options for your lunch.")
    for i in range(len(current_menu)):
        print(f"{i + 1}. {current_menu[i]}")

def remove(current_menu):
    remove_option = input("What would you like to remove in the option?: ")
    for menu in current_menu:
        if menu == remove_option:
            current_menu.remove(menu)
        

def mini_menu():
    while True:
        try:
            print("\nMini Menu List:")
            print("1. Add a new option")
            print("2. Show all options")
            print("3. Pick a random lunch")
            print("4. Remove an option")
            print("5. Exit\n")

            user_choice = int(input("Please choose between 1 and 5: "))
            if user_choice == 1:
                new_option = input("What's the new option you want to add?: ").title()
                menu.append(new_option)
                menu_option(menu)
            elif user_choice == 2:
                menu_option(menu)
            elif user_choice == 3:
                random_lunch = random.choice(menu)
                print(f"You're random lunch for today is {random_lunch}")
            elif user_choice == 4:
                menu_option(menu)
                remove(menu)
            elif user_choice == 5:
                return f"Thank you! Enjoy your lunch!"
            else:
                print("Invalid input! Please choose between 1 - 5 only!")
        except ValueError as err:
            print(f"Error: {err}, please try again!")

# TODO 2: Prompt a user pick for what to eat for lunch.
mini_menu()