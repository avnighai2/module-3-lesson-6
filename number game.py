import random
playing = True
number = str(random.randint(0,25))

print("i will generate number from 0 to 25, you have to guess one digit at a time")
print("THe game ends when you get the correct answer")

while playing:
    guess = input("Give me your best guess")
    if number == guess:
        print("you won the game")
        print("the number was", number)
        break

    else:
        print("that wasnt right, try again")