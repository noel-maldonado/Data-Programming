# (Reverse a list) The reverse function in Section 10.8 reverses a list by copying it
# to a new list. Rewrite the function that reverses the list passed in the argument and
# returns this list. Write a test program that prompts the user to enter a list of numbers,
# invokes the function to reverse the numbers, and displays the numbers.


def reverse(list):
    numbers_string = ''
    reversed_list = list[::-1]
    for num in reversed_list:
        numbers_string += num + " "
    return numbers_string


numbers_list = input("Enter numbers: ").split()
print(reverse(numbers_list))