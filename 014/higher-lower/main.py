############### The Higher Lower Game #####################

# http://www.higherlowergame.com/
# What gets Googled more?
# A frustratingly addictive game of higher or lower using Google searches.
# The data is based on global monthly searches in 2017.

# The Higher Lower Game:

# Include an ASCII art logos.
# 1st time: Randomize 2 entries from the data list. Make sure that they do not overlap.
# 2nd time an followings: replace the 1st entry by the previous 2nd. Randomize 1 entry from the data list. Make sure that it does not overlap.
# Print the 2 choices including the art logos:
# art.logo +
# Compare A: {name}, a {description}, from {country}.
# art.vs
# Against B: {name}, a {description}, from {country}.
# Who has more followers? Type 'A' or 'B':
# Ask the user "Who has more followers? Type 'A' or 'B': "
# Check user's guess against actual answer.
# If the user is right print "You're right! Current score: x.". Ask again replacing the A choice by the previous B, and generating a new random B choice.
# If the user is wrong print "Sorry, that's wrong. Final score: x-1" and exit the program
# Track the number of successful turns.


#Variables
import random
from art import logo, vs
from game_data import data
from replit import clear
TURNS = 1
LOWER_NUMBER = 1
HIGHER_NUMBER = len(data)
# print(HIGHER_NUMBER)
CONTINUE_PLAYING = True
#I get the error when clearing the screen "TERM environment variable not set."
#SOLUTION: https://stackoverflow.com/questions/52895902/term-environemt-varaible-not-set-error-python
import os
os.environ.get('TERM', '')

#Functions
def initialize_screen(a_data, b_data):
    """Clears the screen and types the logo and limits"""
    # Initialize screen
    # Include an ASCII art logo.
    clear()
    print(logo)
    print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}.")
    print(vs)
    print(f"Against B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}.")

def random_number(l_number, h_number):
    """Returns a random number within the specified range"""
    # With the previous line I see the description of the function when I use it
    r_number = random.randrange(start=l_number, stop=h_number, step=1)
    return r_number


def make_guess():
    #Input guess and make sure it's a'A' or 'B'. Returns the chosen letter
    # Ask the user "Who has more followers? Type 'A' or 'B': "
    continue_making_guess = True
    while continue_making_guess:
        chosen_letter = str(input("Who has more followers? Type 'A' or 'B': "))
        if (chosen_letter.upper() == 'A') or (chosen_letter.upper() == 'B'):
            continue_making_guess = False
            return chosen_letter
        else:
            print("Did not understand your choice. Possible answers are only 'A' or 'B': ")
def check_answer(a_count, b_count):
    #Checks wether the right answer it's a'A' or 'B'. Inputs are the 'follower_count' as integers. Returns the right letter
    if a_count >= b_count:
        right_answer = 'A'
    else:
        right_answer = 'B'
    return right_answer

def check_guess(i_guess, i_answer):
    '''Check guess versus answer and print a message accordingly. A wrong answer sets CONTINUE_PLAYING to False'''
    global CONTINUE_PLAYING
    global TURNS
    # If the user is right print "You're right! Current score: x.". Ask again replacing the A choice by the previous B, and generating a new random B choice.
    if i_guess == i_answer:
        print(f"You're right! Current score: {TURNS}.")
        CONTINUE_PLAYING = True
    # If the user is wrong print "Sorry, that's wrong. Final score: x-1" and exit the program
    else:
        print(f"Sorry, that's wrong. Final score: {TURNS - 1}")
        CONTINUE_PLAYING = False
        #Make sure the rest of the while loop does not execute
        exit(0)

#main

# 1st time: Randomize 2 entries from the data list. Make sure that they do not overlap.
# Start selecting 2 random numbers
choice_a = random_number(LOWER_NUMBER, HIGHER_NUMBER)
# Now setting the value to 0, 1, 49, 50, 51 to check behaviour
#choice_a = 1
#print(f"Choice A is {choice_a}")
choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
#print(f"Choice b is {choice_b}")
# Make sure that the second choice is different to the first one and if not change it
while choice_b == choice_a:
    choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
#   print(f"The new choice b is {choice_b}")

data_a = data[choice_a - 1]
#print(data_a)
#print(data_a['name'])
data_b = data[choice_b - 1]
initialize_screen(data_a, data_b)

while CONTINUE_PLAYING:
    #Input guess
    guess = make_guess()
    #Calculate the right answer
    answer = check_answer(data_a['follower_count'], data_b['follower_count'])
    # print(f"The right answer is {answer}.")
    # Check user's guess against actual answer.
    clear()
    print(logo)
    check_guess(guess, answer)
    # Track the number of successful turns.
    TURNS += 1
    # 2nd time an followings: replace the 1st entry by the previous 2nd. Randomize 1 entry from the data list. Make sure that it does not overlap.
    # Start selecting 2 random numbers
    choice_a = choice_b
    choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
    # Make sure that the second choice is different to the first one and if not change it
    while choice_b == choice_a:
        choice_b = random_number(LOWER_NUMBER, HIGHER_NUMBER)
    data_a = data_b
    data_b = data[choice_b - 1]
    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
    print(vs)
    print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")


'''SOLUTION
from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 
Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

# Generate a random account from the game data.
# Format account data into printable format.
# Ask user for a guess.
# Check if user is correct.
## Get follower count.
## If Statement
# Feedback.
# Score Keeping.
# Make game repeatable.
# Make B become the next A.
# Add art.
# Clear screen between rounds.
'''