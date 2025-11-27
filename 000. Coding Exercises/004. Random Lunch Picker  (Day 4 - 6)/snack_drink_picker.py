import random

snacks = ["Chips", "Cookies", "Fruit", "Nuts"]
drinks = ["Water", "Juice", "Soda", "Tea", "Coffee"]

def add_item(list_item):
    """Add a new item to a list safely."""

    while True:
        add_new_item = input("What do you want to add in the option?: ").strip().title()
        
        if not add_new_item:
            print("You didn't enter anything. Nothing was added.\n")
            return

        if add_new_item in list_item:
            print(f"{add_new_item} is already in the list.\n")
            return

        list_item.append(add_new_item)
        print(f"You have successfully added {add_new_item} in the option.\n")

        add_again = input("Do you want to add another item?: Type 'y' or 'n': ").strip().lower()
        
        if add_again != "y":
            break


def show_all_items(items, item_type):
    """
    Display all items in a list as a comma-separated string.
    
    Parameters:
    - items: list of items (e.g., snacks or drinks)
    - item_type: string to describe the type (e.g., "Snacks", "Drinks")
    """
    if not items:
        print(f"No {item_type.lower()} available.\n")
        return

    items_str = ", ".join(items)
    print(f"Here is the list of all {item_type.lower()}!")
    print(f"{item_type}: {items_str}.\n")


# Show a mini menu:
print("Welcome to Random Snack and Drink Picker!")
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