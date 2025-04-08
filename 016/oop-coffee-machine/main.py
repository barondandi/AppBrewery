############### OOP Coffee Machine Program #####################
'''
Requirements
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.

3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.

5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
'''
from random import choice

# Imported libraries
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from art import logo
from replit import clear

# Variables
MENU = Menu()
#PRODUCTS = MENU.get_items()
RESOURCES = CoffeeMaker()
MONEY =  MoneyMachine()
#COIN_TYPES = list(MONEY.COIN_VALUES.keys())
CONTINUE_SERVICE = True
'''
print(MENU)
print(PRODUCTS)
print(RESOURCES)
print(MONEY)
print(COIN_TYPES)
'''

#Functions
def initialize_screen():
    """Clears the screen and types the logo"""
    # Initialize screen
    # Include an ASCII art logo.
    clear()
    print(logo)

#main
# Initialize screen
initialize_screen()

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while CONTINUE_SERVICE:
    #Input command
    OPTIONS = MENU.get_items()
    command = input(f"What would you like? ({OPTIONS}): ").lower()

#    print(command)
    if command == "report":
        RESOURCES.report()
        MONEY.report()
    elif command in MENU.get_items():
        COFFEE_CHOICE = MENU.find_drink(command)
        if COFFEE_CHOICE == True:
            if RESOURCES.is_resource_sufficient(COFFEE_CHOICE):
                if MONEY.make_payment(COFFEE_CHOICE.cost):
                   RESOURCES.make_coffee(COFFEE_CHOICE)
    elif command == "off":
        #2. Turn off the Coffee Machine by entering “off” to the prompt.
        #a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
        CONTINUE_SERVICE = False

'''
ssues:
MENU.get_items(): This method returns the items in the menu as a string, separated by slashes (/). When you're checking if a command is valid (command in MENU.get_items()), you're comparing the input against a string like "espresso/latte/cappuccino", which won't work as expected. You should split the string into individual drink names to check for validity.

COFFEE_CHOICE = MENU.find_drink(command): You're calling find_drink() method, which returns a MenuItem object if the drink is found. However, you're checking if COFFEE_CHOICE == True, which is incorrect. find_drink() will never return True. You should check if COFFEE_CHOICE is not None.

MONEY.make_payment(COFFEE_CHOICE.cost): This is fine, but make_payment already takes care of checking if the user has enough money. The logic inside the loop should be simpler by directly checking if the payment is successful.

RESOURCES.is_resource_sufficient(COFFEE_CHOICE): The check on resources is good, but the is_resource_sufficient() method is supposed to return True or False and print a message if resources are insufficient. You should call this method inside a conditional to confirm it returns True before proceeding with the next steps.
'''

'''
from random import choice
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from replit import clear

# Initialize the Menu, CoffeeMaker, and MoneyMachine objects
MENU = Menu()
RESOURCES = CoffeeMaker()
MONEY = MoneyMachine()

CONTINUE_SERVICE = True

def initialize_screen():
    """Clears the screen and types the logo"""
    # Initialize screen
    clear()
    print(logo)

# Main loop
initialize_screen()

while CONTINUE_SERVICE:
    # Show available drinks and prompt the user for a choice
    OPTIONS = MENU.get_items().strip("/")
    command = input(f"What would you like? ({OPTIONS}): ").lower()

    if command == "report":
        # Print current resources and money
        RESOURCES.report()
        MONEY.report()

    elif command in [item.name for item in MENU.menu]:  # Check if valid choice
        # Find the chosen drink
        COFFEE_CHOICE = MENU.find_drink(command)
        
        if COFFEE_CHOICE:  # Ensure drink was found
            if RESOURCES.is_resource_sufficient(COFFEE_CHOICE):  # Check if enough resources
                if MONEY.make_payment(COFFEE_CHOICE.cost):  # Check if enough money was inserted
                    RESOURCES.make_coffee(COFFEE_CHOICE)  # Make the coffee

    elif command == "off":
        # Stop the coffee machine
        CONTINUE_SERVICE = False
'''