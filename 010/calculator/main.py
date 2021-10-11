from art import logo

print(logo)

# Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

#Function to select operator. Need to define it, so that it can be reused
def select_operator():
    operation_symbol_error = True
    while operation_symbol_error:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above: ")
        if operation_symbol in operations:
            operation_symbol_error = False
            return operation_symbol
        else:
            print("Invalid operator.")

num1 = int(input("What's the first number?: "))
operation_choice = select_operator()
num2 = int(input("What's the second number?: "))
first_answer = operations[operation_choice](num1, num2)

print(f"{num1} {operation_choice} {num2} = {first_answer}")

#Do another operation with the previous result
continue_calculations = True
while continue_calculations:
    continue_selection = (input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to exit\n")).lower()
    if continue_selection == "y":
        print("Pick another operation:")
        operation_choice = select_operator()
        num3 = int(input("What's the next number?: "))
        second_answer = operations[operation_choice](first_answer, num3)
        print(f"{first_answer} {operation_choice} {num3} = {second_answer}")
        first_answer = second_answer
    else:
        continue_calculations = False