#Write your code below this line 👇
from math import ceil

# Two ways of rounding up a number:
# import math
# print(int(math.ceil(4.2)))
# Second way:
# int(21 / 5) + (21 % 5 > 0)
# The first part becomes 4 and the second part evaluates to "True" if there is a remainder, which in addition True = 1; False = 0.

def paint_calc(height, width, cover):
    number_of_cans = ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

''' SOLUTION
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")
'''
