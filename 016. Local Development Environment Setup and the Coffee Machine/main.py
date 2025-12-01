# Program Requirement
# 1. Print Report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make coffee

from coffee_data import resources, menu

# ---------- 1. PRINT REPORT ---------- #
def print_report():
    """Print the current resources of the coffee machine."""
    print("Coffee current resources")
    for key, value in resources.items():
        if key == "water" or key == "milk":
            unit = "ml"
        elif key == "coffee":
            unit = "g"
        else:
            unit = ""
        print(f"{key.title()}: {value}{unit}")

# ---------- 2. CHECK RESOURCES SUFFICIENT ---------- #
def check_resources(available_resources, drink_ingredients):
    """Return True if there are enough resources to make the drink, otherwise False."""
    for ingredient, required_amount in drink_ingredients.items():
        available_amount = available_resources.get(ingredient, 0)

        if available_amount < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


# ---------- 3. PROCESS COINS ---------- #
def process_coins():
    """Ask the user to insert coins and return the total amount."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters? (₱0.25): "))
        dimes = int(input("How many dimes? (₱0.10): "))
        nickels = int(input("How many nickels? (₱0.05): "))
        pennies = int(input("How many pennies? (₱0.01): "))
    except ValueError:
        print("Invalid coin input. Treating as 0.")
        return 0

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


# ---------- 4. CHECK TRANSACTION SUCCESSFUL ---------- #
def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is enough, otherwise False. Also handle change display."""
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ₱{change} in change.")
    return True


# ---------- 5. MAKE COFFEE ---------- #
def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from resources and 'make' the coffee."""
    for ingredient, amount in drink_ingredients.items():
        resources[ingredient] -= amount
    print(f"Here is your {drink_name} ☕. Enjoy!")


# ---------- MAIN PROGRAM LOOP ---------- #
machine_on = True

while machine_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino) or 'report' or 'off': ").lower()

    if user_prompt == "off":
        # Turn off the machine
        machine_on = False

    elif user_prompt == "report":
        # 1. Print report
        print_report()

    elif user_prompt in menu:
        # Get drink data from menu
        drink = menu[user_prompt]
        drink_ingredient = drink["ingredients"]
        drink_costs = drink["cost"]

        # 2. Check resources sufficient?
        if not check_resources(resources, drink_ingredient):
            continue  # Not enough resources, go back to start of loop

        # 3. Process coins
        payment = process_coins()

        # 4. Check transaction successful?
        if not is_transaction_successful(payment, drink_costs):
            continue  # Payment failed, go back to start of loop

        # 5. Make coffee
        make_coffee(user_prompt, drink_ingredient)

    else:
        print("Invalid choice. Please select espresso, latte, cappuccino, report, or off.")
