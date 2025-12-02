menu = {
    "espresso": {
        "ingredients": {
            "water" : 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def report(user_choice):
    for key, value in resources.items():
        if key == "water" or key == "milk":
            unit = "ml"
        elif key == "coffee":
            unit = "g"
        else:
            unit = " "

        print(f"{key} : {value}{unit}")
    print(f"Money: ${profit}")

def check_resources(available_resources, coffee_ingredients):
    """Return True if there are enough resources to make the drink, otherwise False."""
    for ingredient, required_amount in coffee_ingredients.items():
        available_amount = available_resources.get(ingredient, 0)

        if available_amount < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False

    print("Yey! We have enough resources. Please make a payment.")
    return True


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break

    elif choice == "report":
        report(choice)

    elif choice in menu:
        drink = menu[choice]
        drink_ingredients = drink["ingredients"]
        drink_costs = drink["cost"]

        if not check_resources(resources, drink_ingredients):
            continue