print("Hello")

num_char = len("Hello")
print(num_char)

def my_function():
    print("Hello")
    print("Bye")

my_function()

'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
'''

'''
Hurdles race
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for jumps in range(1, 7):
# for jumps in range(6):
    jump()

# Other way is with the while loop
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
'''