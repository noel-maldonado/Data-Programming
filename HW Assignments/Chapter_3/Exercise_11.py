#(Reverse number) Write a program that prompts the user to enter a four-digit integer
#and displays the number in reverse order. Here is a sample run:
userNumber = eval(input("Enter an integer: "))
reversedNumber = str(userNumber % 10)
userNumber //= 10
reversedNumber += str(userNumber % 10)
userNumber //= 10
reversedNumber += str(userNumber % 10) + str(userNumber // 10)
print(reversedNumber)