# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total. Here is a sample run:
#
# Enter the subtotal and a gratuity rate:  15.69, 15
# The gratuity is 2.35 and the total is 18.04
subtotal = eval(input('Enter Subtotal: '))
gratuityRate = eval(input('Enter gratuity rate (15 = 15%): '))
gratuity = int((subtotal * (gratuityRate / 100.0)) * 100) / 100.0
total = subtotal + gratuity
print('The gratuity is', gratuity, 'and the total is', total)