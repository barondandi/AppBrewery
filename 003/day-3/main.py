print("Welcome to the rollercaster.")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child ticket are $5.")
    elif age <=18:
        print("Youth ticket are $7.")
    else:
        print("Adult ticket are $12.")
else:
    print("Sorry, you need to grow taller before you can ride.")