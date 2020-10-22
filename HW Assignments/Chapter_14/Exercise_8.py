# (Display nonduplicate words in ascending order) Write a program that prompts
# the user to enter a text file, reads words from the file, and displays all the nonduplicate
# words in ascending order.


user_string = input("Enter a string of words: ")

words = user_string.split()
nonduplicateWords = set(words)
words = list(nonduplicateWords)
words.sort()

for word in words:
    print(word, end=" ")