# (Reverse the numbers entered) Write a program that reads a list of integers and
# displays them in the reverse order in which they were read.

numbers = input("Enter list of integers: ")
numbersList = [int(s) for s in numbers.split()]

print('Your list', numbersList, 'reversed is', numbersList[::-1])