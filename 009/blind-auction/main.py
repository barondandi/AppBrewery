from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

#Clear screen andd print logo
clear()
print(logo)
print("Welcome to the secret auction program.")

#Initialize variables
bids = {}
continue_bidding = True

#Define function to add bids
def add_bid():
    bid_name = str(input("What is your name?: "))
    bid_amount = int(input("What's your bid?: $ "))
    bids[bid_name] = bid_amount
    bid_continue = (str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))).lower()
    if bid_continue == "no":
        return False
    else:
        return True

#Define a function to check the winner and print it
def check_winner(bid_dictionary):
    bid = 0
    for name in bid_dictionary:
        if bid_dictionary[name] > bid:
            winner = name
            bid = bid_dictionary[name]
    print(f"The winner is {winner} with a bid of ${bid}.")

#Main code
while continue_bidding:
    continue_bidding = add_bid()
    clear()
#print(bids)
check_winner(bid_dictionary = bids)