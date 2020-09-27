# (Sort three numbers) Write the following function to display three numbers in
# increasing order:
# def displaySortedNumbers(num1, num2, num3):
# Write a test program that prompts the user to enter three numbers and invokes the
# function to display them in increasing order. Here are some sample runs:


def displaySortedNumbers(i1, i2, i3):
    max = ''
    min = ''
    mid = ''
    if i1 > i2 > i3:
        max = str(i1)
        min = str(i3)
        mid = str(i2)
    elif i2 > i3 > i1:
        max = str(i2)
        min = str(i1)
        mid = str(i3)
    elif i3 > i1 > i2:
        max = str(i3)
        min = str(i2)
        mid = str(i1)
    elif i3 > i2 > i1:
        max = str(i3)
        min = str(i1)
        mid = str(i2)
    elif i2 > i1 > i3:
        max = str(i2)
        min = str(i3)
        mid = str(i1)
    elif i1 > i3 > i2:
        max = str(i1)
        min = str(i2)
        mid = str(i3)
    print("The sorted numbers are ", min, mid, max)


i1, i2, i3 = eval(input('Enter three digits (seprate with a comma): '))

displaySortedNumbers(i1, i2, i3)
