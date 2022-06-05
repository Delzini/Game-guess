import random


options = ["rock","paper","scissors"]
computer = random.choice(options)
player = None
while (player not in options or player == computer):
    print("Are you ready for a guess game?")
    print("Choose from our collections of option")
    print("Rock , Paper or Scissors")
    player = input("").lower()
    if player == computer:
        print("Player (%s) : CPU (%s)" %(player,computer))
        print("Nice Guess - 'Game Tie' \nTry Again!Try Again!!Try Again!!!")
    elif player == "rock":
        if computer == "paper":
            print("Player (%s) : CPU (%s)" %(player,computer))
            print("You Lose")
        if computer == "scissors":
            print("Player (%s) : CPU (%s)" %(player,computer))
            print("Congratulations : You Win")
    elif player == "paper":
        if computer == "scissors":
            print("Player (%s) : CPU (%s)" %(player,computer))
            print("You Lose")
        if computer == "rock":
            print("Player (%s) : CPU (%s)" %(player,computer))
            print("Congratulations : You Win")
    elif player == "scissors":
        if computer == "rock":
            print("Player (%s) : CPU (%s)" %(player,computer))
            print("You Lose")
        if computer == "paper":
            print("Player (%s) : CPU (%s)" %(player,computer))
            print("Congratulations : You Win")
else:
    print("Game Over!")
    