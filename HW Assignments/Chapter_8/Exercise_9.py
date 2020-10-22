# (Binary to hex) Write a function that parses a binary number into a hex number.
# The function header is:
# def binaryToHex(binaryValue):
# Write a test program that prompts the user to enter a binary number and displays
# the corresponding hexadecimal value.

def f(x):
    return {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }[x]


def binaryToHex(binaryValue):
    binary = binaryValue[::-1]
    hex = ""
    while len(binary) > 0:
        currentBinary = binary[0:4]
        decimal = 0
        for i in range(len(currentBinary)):
            decimal += int(currentBinary[i]) * 2 ** i
        hex += f(decimal)
        binary = binary[4:len(binary)]
    hex = hex[::-1]
    return hex


binary = input("Enter a binary String: ")
print(binaryToHex(binary))

# 11101100101001 should equal 3B29
