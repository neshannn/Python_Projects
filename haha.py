import random

def get_choices():
    player_choice = input("enter a choice (rock, paper, scissors: )")
    option = ["rock", "paper", "scissors"]
    computer_choice = random.choices(option)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}") 
    if player==computer:
        return "its a tie!"
    elif player == "rock":
      if computer == "scissors":
        return "rock smashes scissors! You Win !"
    else:
         return "paper covers rock! You LOose."
    elif: player
check_win("rock", "paper")