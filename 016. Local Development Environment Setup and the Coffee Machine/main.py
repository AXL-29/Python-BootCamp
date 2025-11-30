# Program Requirement
    # 1. Print Report
    # 2. Check resources sufficient?
    # 3. Process coins
    # 4. Check transaction successful?
    # 5. Make coffee

from coffee_data import resources, menu

def check_resources(coffee_resources, coffee_menu):
    for key, value in coffee_menu.items():
        if key > coffee_resources.key():
            print("invalid")


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
            unit = ""   # no unit if your don't need one.
        print(f"{key.title()}: {value}{unit}")

# TODO: 2. Check resources sufficient to make a coffee order.

