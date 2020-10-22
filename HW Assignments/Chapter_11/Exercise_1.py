# (Sum elements column by column) Write a function that returns the sum of all the
# elements in a specified column in a matrix using the following header:
# def sumColumn(m, columnIndex):
# Write a test program that reads a matrix and displays the sum of each column.

def sumColumn(m, columnIndex):
    sum = 0
    for row in range(len(m)):
        sum += m[row][columnIndex]

    return sum

matrix = []

for i in range(3):
    row = input("Enter a 3-by-4 matrix row for row " + str(i)+": ").split()
    matrix.append([float(x) for x in row])

for columnIndex in range(4):
    sum = sumColumn(matrix, columnIndex)
    print("Sum of the elements for column", columnIndex, 'is', sum)

