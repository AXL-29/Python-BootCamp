from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
coffee_menu = Menu()

machine_on = True

while machine_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino) or 'report' or 'off': ").lower()

    if user_prompt == "off":
        # Turn off the machine
        machine_on = False

    elif user_prompt == "report":
        # 1. Print report
        coffee.report()

    elif user_prompt in coffee_menu.get_items():
        coffee_menu.find_drink(user_prompt)

    else:
        print("Invalid choice. Please select espresso, latte, cappuccino, report, or off.")
