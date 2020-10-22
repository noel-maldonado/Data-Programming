# (Check SSN) Write a program that prompts the user to enter a Social Security
# number in the format ddd-dd-dddd, where d is a digit. The program displays
# Valid SSN for a correct Social Security number or Invalid SSN otherwise.

ssn = input("Enter a valid social security number (ddd-dd-dddd): ")

if len(ssn) == 11 and ssn[0:3].isdigit() and ssn[4:6].isdigit() and ssn[7:11].isdigit():
    print("You entered a valid SSN")
else:
    print("You entered a invalid SSN")