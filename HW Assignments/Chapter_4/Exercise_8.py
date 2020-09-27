#(Sort three integers) Write a program that prompts the user to enter three integers
#and displays them in increasing order.

i1 = eval(input("Enter the first interger: "))
i2 = eval(input("Enter the second interger: "))
i3 = eval(input("Enter the third interger: "))
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

print(min, mid, max)