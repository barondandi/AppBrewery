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
    bid_amount = int(input("What's your bid?: $"))
    bids[bid_name]: bid_amount
    print(bids)
    bid_continue = (str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))).lower()
    if bid_continue == "no":
        continue_bidding = False
    clear()

#Main code
while continue_bidding:
    add_bid()