from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the required classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

'''
🧠 What Changed in the OOP Version?
Feature	Functional Approach	Object-Oriented Approach
Menu data	Stored in a dictionary (MENU)	Encapsulated in MenuItem and Menu classes
Resource management	Used a global resources dictionary	Encapsulated in CoffeeMaker class
Money handling	Used global money and coin handling	Managed by MoneyMachine class with internal methods
Code structure	Functions with global state	Encapsulated methods with clearly defined interfaces
Scalability	Harder to maintain or expand	Easy to extend with new drinks or features
'''