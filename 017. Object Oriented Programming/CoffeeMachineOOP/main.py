from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    user_prompt = input(f"What would you like? ({options}): ").lower()

    if user_prompt == "off":
        break

    elif user_prompt == "report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(user_prompt):
        if coffee_maker.is_resource_sufficient(menu.find_drink(user_prompt)):
            if money_machine.make_payment(menu.find_drink(user_prompt).cost):
                coffee_maker.make_coffee(menu.find_drink(user_prompt))
