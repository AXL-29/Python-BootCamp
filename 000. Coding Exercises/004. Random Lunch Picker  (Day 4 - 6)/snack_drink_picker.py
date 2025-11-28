import random

snacks = ["chips", "cookies", "fruit", "nuts"]
drinks = ["water", "juice", "soda", "tea", "coffee"]

def add_item(list_item):
    """Add a new item to a list safely."""
    while True:
        add_new_item = input("What do you want to add in the option?: ").strip().lower()
        
        if not add_new_item:
            print("You didn't enter anything. Nothing was added.\n")
            return

        if add_new_item in list_item:
            print(f"{add_new_item} is already in the list.\n")
            return

        list_item.append(add_new_item)
        print(f"You have successfully added {add_new_item} in the option.\n")

        add_again = input("Do you want to add another item? (y/n): ").strip().lower()
        if add_again != "y":
            break

def show_all_items(items, item_type):
    """Display all items in a list as a comma-separated string."""
    if not items:
        print(f"No {item_type.lower()} available.\n")
        return

    items_str = ", ".join(items)
    print(f"Here is the list of all {item_type.lower()}!")
    print(f"{item_type}: {items_str.title()}.\n")

def random_snack_drinks(snacks, drinks):
    """Pick a random snack and drink, handling empty lists."""
    if not snacks:
        return "There are no snacks available. Please add some snacks first."
    if not drinks:
        return "There are no drinks available. Please add some drinks first."

    snacks_drinks = [random.choice(snacks), random.choice(drinks)]
    snacks_drinks_str = ", ".join(snacks_drinks)
    return f"Your random snacks and drinks are: {snacks_drinks_str.title()}"

def remove(list_item, item_type):
    """Remove an option by name, handling non-existent names."""
    if not list_item:
        print(f"The {item_type.lower()} list is currently empty. Nothing to remove.\n")
        return

    while True:
        # Show current items before asking what to remove
        show_all_items(list_item, item_type)

        remove_item = input(f"What do you want to remove from the {item_type.lower()}?: ").strip().lower()
        
        if not remove_item:
            print("You didn't enter anything. Nothing was removed.\n")
            return
        
        if remove_item in list_item:
            list_item.remove(remove_item)
            print(f"You have removed {remove_item} from the {item_type.lower()}.\n")

            # Show updated list after removal
            show_all_items(list_item, item_type)

            remove_again = input("Do you want to remove another item? (y/n): ").strip().lower()
            if remove_again != "y":
                break
        else:
            print(f"{remove_item} is not in the {item_type.lower()} list.\n")
            try_again = input("Do you want to try another name? (y/n): ").strip().lower()
            if try_again != "y":
                break


def mini_menu():
    """Display and handle the Random Snack and Drink Picker mini menu."""
    print("Welcome to Random Snack and Drink Picker!")

    user_choice = 0
    while user_choice != 8:
        print("1. Add a new snack")
        print("2. Add a new drink")
        print("3. Show all snacks")
        print("4. Show all drinks")
        print("5. Pick a random snack & drink")
        print("6. Remove a snack")
        print("7. Remove a drink")
        print("8. Exit\n")

        while True:
            try:
                user_choice = int(input("Please enter a number between 1 and 8: "))
                if 1 <= user_choice <= 8:
                    break
                else:
                    print("Invalid input! Number must be between 1 and 8.")
            except ValueError as err:
                print(f"Error: {err}, Please try again!")

        if user_choice == 1:
            add_item(snacks)
            show_all_items(snacks, "Snacks")
        elif user_choice == 2:
            add_item(drinks)
            show_all_items(drinks, "Drinks")
        elif user_choice == 3:
            show_all_items(snacks, "Snacks")
        elif user_choice == 4:
            show_all_items(drinks, "Drinks")
        elif user_choice == 5:
            print(random_snack_drinks(snacks, drinks))
        elif user_choice == 6:
            remove(snacks, "Snacks")
        elif user_choice == 7:
            remove(drinks, "Drinks")
        else:
            print("Thank you for using Random Snack and Drink Picker! Enjoy!")

# Main Loop for Mini Menu
mini_menu()
