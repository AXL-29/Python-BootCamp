# Program Requirement
    # 1. Print Report
    # 2. Check resources sufficient?
    # 3. Process coins
    # 4. Check transaction successful?
    # 5. Make coffee

from coffee_data import resources, menu


def check_resources(coffee_resources, coffee_menu):
    for ingredient, required_amount in coffee_menu.items():
        available_amount = coffee_resources.get(ingredient, 0)

        if available_amount < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    print("We have enough resources!")
    return True


user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 1. Print report of all coffee machine resources.
if user_prompt == "report":
    print("Coffee current resources")
    for key, value in resources.items():
        if key == "water" or key == "milk":
            unit = "ml"
        elif key == "coffee":
            unit = "g"
        else:
            unit = ""
        print(f"{key.title()}: {value}{unit}")

# TODO: 2. Check resources sufficient to make a coffee order.
elif user_prompt in menu:
    # get the ingredients needed for that drink
    drink = menu[user_prompt]
    ingredients_needed = drink["ingredients"]

    # call your check_resources function
    if check_resources(resources, ingredients_needed):
        print(f"Making your {user_prompt} ☕...")
        # later: you'll subtract the ingredients from resources here
else:
    print("Invalid choice.")
