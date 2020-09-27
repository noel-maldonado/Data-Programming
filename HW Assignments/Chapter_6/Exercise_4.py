# (Display an integer reversed) Write the following function to display an integer in
# reverse order:
# def reverse(number):


def reverse(number):
    reversedNumber= ''
    while number > 0:
        reversedNumber += str(number % 10)
        number //= 10
    print(reversedNumber)

userInput = eval(input("Enter an integer: "))
print("The integer reveresed is: ", end="")
reverse(userInput)
