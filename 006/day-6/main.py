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

''' Hurdle 2
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
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

while at_goal() == False:
    jump()

# I could also have used 
# while not at_goal(): 
'''

# When to use for or while loops
fruits = ["Apple", "Pear", "Orange"]
for fruit in fruits:
    print(fruit)

for n in range(1, 6):
    print(n)

''' Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
'''

''' Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    height = 0
    while not right_is_clear():
        move()
        height += 1
    turn_right()
    move()
    turn_right()
    while height > 0:
        move()
        height -= 1
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

# Other option:
# While front_is_clear()
#   move()
'''

''' Escaping the maze
n&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''

''' Maze whith infinite loop detection
def turn_right():
    turn_left()
    turn_left()
    turn_left()

loop_counter = 0

while not at_goal():
    if right_is_clear():
        if loop_counter < 4:
            turn_right()
            move()
            loop_counter += 1
        else:
            turn_right()
            loop_counter = 0
    elif front_is_clear():
        move()
        loop_counter = 0
    else:
        turn_left()
        loop_counter = 0

# Other solution is adding before the while loop:
# while front_is_clear():
#   move()
# turn_left()
'''