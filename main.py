import random

moves = ('Rock','Paper', 'Scissors')

quit  = False

while not quit:
    userMove = input('Rock, Paper, or Scissors? Enter "q" or "Q" to quit:\n')
    if userMove == "q" or userMove == "Q":
        quit = True
    else:
        userMove = userMove.title()
        computerMove = random.choice(moves)
        if userMove not in moves:
            print("Incorrect input")
        elif (userMove == "Rock" and computerMove == "Scissors") or (userMove == "Paper" and computerMove == "Rock"):
            print(f"Your move: {userMove}")
            print(f"Computer Move: {computerMove}")
            print("You Win")
        elif (userMove == "Paper" and computerMove == "Scissors") or (userMove =="Scissors" and computerMove == "Rock"):
            print(f"Your move: {userMove}")
            print(f"Computer Move: {computerMove}")
            print("You lose")
        else:
            print(f"Your move: {userMove}")
            print(f"Computer Move: {computerMove}")
            print("Draw")