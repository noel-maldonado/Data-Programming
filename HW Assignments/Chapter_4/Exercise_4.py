#(Game: learn addition) Write a program that generates two integers under 100 and
#prompts the user to enter the sum of these two integers. The program then reports
#true if the answer is correct, false otherwise. The program is similar to Listing 4.1.

import random

number1 = random.randint(1, 99)
number2 = random.randint(1, 99)

question = 'What is ' + str(number1) + ' + ' + str(number2) + '? '
answer = number1 + number2
userAnswer = eval(input(question))
questionWithUserAnswer = str(number1) + ' + ' + str(number2) + ' = ' + str(userAnswer)
if userAnswer == answer:
    print("Correct!\n" + questionWithUserAnswer)
else:
     print("Incorrect")
