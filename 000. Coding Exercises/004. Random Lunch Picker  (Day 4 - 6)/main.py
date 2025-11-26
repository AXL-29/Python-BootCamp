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

def menu_list(current_menu):
    print("Here's the available options for your lunch.")
    for option in current_menu:
        number_list = menu.index(option)
        number_list += 1
        print(f"{number_list}. {option}")

def remove(current_menu):
    valid = False

    while not valid:
        remove_option = input("What would you like to remove in the current menu?: ").title()
        for option in current_menu:
            if remove_option == option:
                current_menu.remove(option)
                print(menu_list(current_menu))
                valid = True
                break

            else:
                print(f"You have typed {remove_option}, which is not in the menu list, please try again!")
                valid = False


def mini_menu(user_choice):
    if user_choice == 1:
        new_option = input("What's the new option you want to add?: ").title()
        menu.append(new_option)
        menu_list(menu)
    elif user_choice == 2:
        menu_list(menu)
    elif user_choice == 3:
        random_lunch = random.choice(menu)
        print(f"You're random lunch for today is {random_lunch}")
    elif user_choice == 4:
        menu_list(menu)
        remove(menu)
# TODO 2: Prompt a user pick for what to eat for lunch.
print("Mini Menu List:")
print("1. Add a new option")
print("2. Show all options")
print("3. Pick a random lunch")
print("4. Remove an option")
print("5. Exit")

user_pick = int(input("Please choose between 1 and 5: "))
mini_menu(user_pick)