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

def payment_process():
    """Ask the user to insert coins and return the total amount."""
    print("Please insert coins.")

    try:
        quarters = int(input("How many quarters? ($0.25): "))
        dimes = int(input("How many dimes? ($0.10): "))
        nickels = int(input("How many nickels ($0.05): "))
        pennies = int(input("How many pennies ($0.01): "))
    except ValueError:
        print("Invalid input, treating as 0")
        return 0

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is enough, otherwise False. Also handle change display."""
    if money_received < drink_cost:
        print("Sorry not enough money. Money refunded.")
        return False
    
    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here's ${change} in change.")
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
        
        payment = payment_process()

        if not is_transaction_successful(payment, drink_costs):
            continue
