#(Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
#game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
#wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
#scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
#2 and displays a message indicating whether the user or the computer wins, loses,
#or draws. Here are sample runs:
import random

userPick = eval(input("scissors(0), rock(1), paper(2): "))
randomPick = random.randrange(0, 2)
if userPick == randomPick:
    if userPick == 0:
        print("The computer is scissors. You are scissors. It is a draw")
    elif userPick == 1:
        print("The computer is rock. You are rock. It is a draw")
    else:
        print("The computer is paper. You are paper. It is a draw")
elif userPick < randomPick:
    if userPick != 1 and randomPick == 2:
        print("The computer is paper. You are scissors. You won")
    elif randomPick == 1:
        print("The computer has rock. You have scissors. You lost.")
    else:
        print("The computer is paper. You are rock. You lost")
elif userPick > randomPick:
    if userPick == 2 and randomPick == 1:
        print("The computer is rock. You are paper. You won.")
    elif userPick == 1:
        print("The computer is scissors. You are rock. You won.")
    else:
        print("The computer is  scissor. You are paper. You lost.")