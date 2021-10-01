import random
from password_art import logo
from password_words import word_list
# from password_words_test_20 import word_list
from password_vars import number_of_words, seconds_per_round
# Import function to clear the screen
from replit import clear
#Import function to count time
from time import sleep


# Initialize variables
game_is_finished = False
word_list_len = len(word_list) - 1
# print(word_list[word_list_len])
game_round = 1

# Create list to check which words have already been used
used_words = []
for index in range(word_list_len):
    used_words.append(False)
used_words_counter = len(used_words)
# print(used_words)
# print(len(used_words))
# print(type(used_words[word_list_len - 1]))

#Define function to work as a countdown timer
def stopwatch(seconds_left):
    while seconds_left:
        minn, secc = divmod(seconds_left, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        sleep(1)
        seconds_left -= 1

# Initialize program
print(logo)
print(f"Dictionary has {word_list_len} words. Each round will show {number_of_words} words and will last {seconds_per_round} seconds.\n")

# Loop to keep on generating words unless told otherwise
while not game_is_finished:
    # Generate random unused words
    word_counter = number_of_words
    words_chosen = []
    while word_counter > 0 and used_words_counter > 0:
        word_index = random.randint(0, word_list_len - 1)
        if not used_words[word_index]:
            used_words[word_index] = True
            words_chosen.append(word_list[word_index])
            word_counter -= 1
            used_words_counter -= 1
    if used_words_counter < 1:
        print("Sorry, all words have been already used!")
        game_is_finished = True
    else:
        print(f"WORDS CHOSEN FOR ROUND {game_round}: {words_chosen}\n")
        game_round += 1
        stopwatch(seconds_left = seconds_per_round)
    print("Round time is FINISHED!\n")
    print('Press "ENTER" to continue. Any other letter plus "ENTER" to exit')
    if input() != "":
        game_is_finished = True
    clear()

'''SOLUTION
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
'''