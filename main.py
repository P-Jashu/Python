import random
from art import logo
from replit import clear

def random_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0,12)]

def calculate_score(player_cards):
  if sum(player_cards) == 21 and len(player_cards) == 2:
    return 0 
  if 11 in player_cards and sum(player_cards) > 21:
    player_cards.remove(11)
    player_cards.append(1)
  return sum(player_cards)

def result(user_score, dealer_score):
  if user_score == dealer_score:
    return "It's a draw"
  elif user_score == 0:
    return "You win with a blackjack!!!!"
  elif dealer_score == 0:
    return "You lost, opponent has blackjack"
  elif user_score > 21:
    return "You lost, because of BURST!!!"
  elif dealer_score > 21:
    return "You won, because opponent has BURST"
  elif dealer_score < user_score:
    return "You WON"
  else:
    return "You Lost"

def blackjack():
  print(logo)
  user = []
  dealer = []
  game_over = False
  
  for _ in range(2):
    user.append(random_card())
    dealer.append(random_card())
  
  while not game_over:
    user_score = calculate_score(user)
    dealer_score = calculate_score(dealer)
    print(f"Your cards are {user} and your current total is{user_score}")
    print(f"Dealer cards are {dealer[0]},X")
    
    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_over = True
    else:
      choice = input("Do you want to continue the game?('y' or 'n')")
      if choice == "y":
        user.append(random_card())
      else:
        game_over = True
  
  while dealer_score != 0 and dealer_score < 17:
    dealer.append(random_card())
    dealer_score = calculate_score(dealer)
    print(f"Your final hand is {user} and your final score is {user_score}")
  print(f"dealer's final hand is {dealer} and dealer's final score is {dealer_score}")
  print(result(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()
