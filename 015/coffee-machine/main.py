############### Coffee Machine Program #####################
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

#Variables
from art import logo
from replit import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

products = list(MENU.keys())

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

coin = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}

CONTINUE_SERVICE = True

#Functions

def initialize_screen():
    """Clears the screen and types the logo"""
    # Initialize screen
    # Include an ASCII art logo.
    clear()
    print(logo)

def get_command():
    #Input guess and make sure it's an option of the list, "report" or "off". Returns the chosen option lowercase
    # Ask the user "Who has more followers? Type 'A' or 'B': "
    continue_requesting_command = True
    while continue_requesting_command:
        typed_command = str(input("What would you like? (" + '/'.join(products) +"):"))
        if (typed_command.lower() in products):
            continue_requesting_command = False
            return typed_command.lower()
        elif (typed_command.lower() == "report"):
                continue_requesting_command = False
                return typed_command.lower()
        elif (typed_command.lower() == "off"):
                continue_requesting_command = False
                return typed_command.lower()
        else:
            print("Did not understand your choice. Possible answers are only " + ' or '.join(products))


'''
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
'''
def print_report():
    """Prints a report that shows the current resource values"""
#    print(resources)
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

'''
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
'''
def get_coins():
    print()

#main

# Initializa screen
initialize_screen()

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while CONTINUE_SERVICE:
    #Input command
    command = get_command()
#    print(command)
    if command == "report":
        print_report()
    elif command in products:
        inserted_money = get_coins()
    elif command == "off":
        #2. Turn off the Coffee Machine by entering “off” to the prompt.
        #a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
        CONTINUE_SERVICE = False

'''SOLUTION
'''