# (Count the letters in a string) Write a function that counts the number of letters in
# a string using the following header:
# def countLetters(s):
# Write a test program that prompts the user to enter a string and displays the number
# of letters in the string.

def countLetters(userString):
    letter_count = 0
    if userString.isalpha():
        letter_count = len(userString)
    else:
        for char in userString:
            letter_count += 1 if char.isalpha() else False
    return letter_count

userString = input("Enter a string: ")
print("Letters Count:", countLetters(userString))