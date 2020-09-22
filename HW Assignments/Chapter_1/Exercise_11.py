#(Population projection) The US Census Bureau projects population based on the
#following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years. Assume the
# current population is 312032486 and one year has 365 days. Hint: in Python, you
# can use integer division operator // to perform division. The result is an integer. For
# example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
print('Current Population: 312032486')
print('Seconds in a Year:', (60 * 60 * 24 * 365))
print('')
print('Using the Following Assumptions: ')
print('- One birth every 7 seconds')
print('- One death every 13 seconds')
print('- One new immigrant every 45 seconds')
print('')
print('Each year the population rises approximately by', ((60 * 60 * 24 * 365) // 7) + ((60 * 60 * 24 * 365) // 13) + ((60 * 60 * 24 * 365) // 45), end='.\n')
print('')
print('Population in One Year:', (((60 * 60 * 24 * 365) // 7) + ((60 * 60 * 24 * 365) // 13) + ((60 * 60 * 24 * 365) // 45)) + 312_032_486, end='.\n')
print('Population in Two Years:', (((60 * 60 * 24 * 365) // 7) + ((60 * 60 * 24 * 365) // 13) + ((60 * 60 * 24 * 365) // 45)) * 2 + 312_032_486, end='.\n')
print('Population in Three Years:', (((60 * 60 * 24 * 365) // 7) + ((60 * 60 * 24 * 365) // 13) + ((60 * 60 * 24 * 365) // 45)) * 3 + 312_032_486, end='.\n')
print('Population in Four Years:', (((60 * 60 * 24 * 365) // 7) + ((60 * 60 * 24 * 365) // 13) + ((60 * 60 * 24 * 365) // 45)) * 4 + 312_032_486, end='.\n')
print('Population in Five Years:', (((60 * 60 * 24 * 365) // 7) + ((60 * 60 * 24 * 365) // 13) + ((60 * 60 * 24 * 365) // 45)) * 5 + 312_032_486, end='.\n')
