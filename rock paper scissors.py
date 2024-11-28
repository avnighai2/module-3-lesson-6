import random

while True:
    userAction = input("Enter a choice (Rock, Paper, scissors):")
    possibleAction = ["rock", "paper", "scissors"]
    computerAction = random.choice(possibleAction)
    print(f'\nYou chose {userAction}, computer chose {computerAction}')

    if userAction == computerAction:
        print("Both players selected", userAction, "it's a tie")
    elif userAction == "rock":
        if computerAction == "scissors":
            print("Rock beats Scissors, You win!")
        else:
            print("Paper covers Rock, You lose!")
    elif userAction == "paper":
        if computerAction == "scissors":
            print("paper covers Rock, You win!")
        else:
            print("Scissors cuts paper, You lose!")
    elif userAction == "scissors":
        if computerAction == "rock":
            print("Rock beats Scissors, You lose!")
        else:
            print("Scissors cuts Paper, You win!")
    
    