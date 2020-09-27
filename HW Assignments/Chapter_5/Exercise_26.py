#(Sum a series) Write a program to sum the following series:


sum = 0
for i in range(1, 97 + 1, 2):
    sum += 1.0 * i / (i + 2)
sumFormatted = str(int(sum * 100 ) / 100)

print("The sum is " + sumFormatted)