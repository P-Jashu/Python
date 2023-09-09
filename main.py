from replit import clear
from art import logo
print(logo)
print("\nWelcome to my auction")
bidding = False
bid = {}

def winner(bid):
  max_bid = 0
  winner_name = ""
  for i in bid:
    if bid[i] > max_bid:
      max_bid = bid[i]
      winner_name = i
  print(f"\nThe highest bidder is {winner_name} with amount of ${max_bid}")

while not bidding:
  name = input("\nEnter your name: ")
  price = int(input("\nEnter your amount: $"))
  bid[name] = price
  next_bid = input("\nAny one else is there to bid? (yes or no)")
  if next_bid == "no":
    winner(bid)
    choice = input("\nDo you want to see other bids as well?(yes or no) ")
    if choice == "yes":
      print(bid)
    bidding = True
  else:
    clear()
    print(logo)
