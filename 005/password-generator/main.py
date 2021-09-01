#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Initialize password
password = ""

for index in range(0, nr_letters):
    rnd_char = letters[random.randint(0, len(letters) - 1)]
    # print(rnd_char)
    password = password + rnd_char

for index in range(0, nr_symbols):
    rnd_char = symbols[random.randint(0, len(symbols) - 1)]
    password = password + rnd_char

for index in range(0, nr_numbers):
    rnd_char = numbers[random.randint(0, len(numbers) - 1)]
    password = password + rnd_char

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

nr_total = nr_letters + nr_symbols + nr_numbers

# Initialize counters for each of the type of characters
left_letters = nr_letters
left_symbols = nr_symbols
left_numbers = nr_numbers
password = ""

for index in range(0, nr_total):
    chars_left = False
    while chars_left == False:
        char_type = random.randint(1, 3)
        if char_type == 1 and left_letters !=0:
            left_letters -= 1
            chars_left = True
        elif char_type == 2 and left_symbols !=0:
            left_symbols -= 1
            chars_left = True
        elif char_type == 3 and left_numbers != 0:
            left_numbers -= 1
            chars_left = True
    if char_type == 1:
        rnd_char = letters[random.randint(0, len(letters) - 1)]
    elif char_type == 2:
        rnd_char = symbols[random.randint(0, len(symbols) - 1)]
    else:
        rnd_char = numbers[random.randint(0, len(numbers) - 1)]
    password = password + rnd_char

print(password)
