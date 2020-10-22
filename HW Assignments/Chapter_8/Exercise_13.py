# (Longest common prefix) Write a method that returns the longest common prefix
# of two strings. For example, the longest common prefix of distance and
# disinfection is dis. The header of the method is:
# def prefix(s1, s2)
# If the two strings have no common prefix, the method returns an empty string.
# Write a main method that prompts the user to enter two strings and displays their
# common prefix.

def prefix(s1, s2):
    commonPrefix = ''
    count = 0
    for char in s1:
        if char == s2[count]:
            commonPrefix += char
        else:
            break
        count += 1
    return commonPrefix

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print(prefix(s1, s2))