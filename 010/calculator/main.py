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

num1 = int(input("What's the first number?: "))

operation_symbol_error = True
while operation_symbol_error:
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation from the line above: ")
    if operation_symbol in operations:
        operation_symbol_error = False
    else:
        print("Invalid operator.")

num2 = int(input("What's the second number?: "))
first_answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

