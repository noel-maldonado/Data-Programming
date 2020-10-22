# (Occurrences of a specified character) Write a function that finds the number of
# occurrences of a specified character in a string using the following header:
# def count(s, ch):
# The str class has the count method. Implement your method without using the
# count method. For example, count("Welcome", 'e') returns 2. Write a test
# program that prompts the user to enter a string followed by a character and displays
# the number of occurrences of the character in the string.

def count(userString, userChar):
    occurrence = 0
    for char in userString:
        if char == userChar:
            occurrence += 1
    return occurrence


userString = input("Enter a String: ")
userChar = input("Enter a Character: ")
print(count(userString, userChar))
