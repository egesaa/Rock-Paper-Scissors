import random

def game():
    user = (input("'r' for rock, 'p' for paper, 's' for scissors: \n")).lower()
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        print(f"Draw, both choices are {user}")
    elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        print(f"Player wins. Player: {user}, Computer: {computer}.")
    else:
        print(f"Player loses. Player: {user}, Computer: {computer}.")
while True:
    game()
