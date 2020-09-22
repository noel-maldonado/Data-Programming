# (Geometry: area of a triangle) Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
# The formula for computing the area of a triangle is
# s = (side1 + side2 + side3) / 2
# area = sqrt(s(s - side1)(s - side2)(s - side3))

x1, y1 = eval(input('Enter First Point (x, y): '))
x2, y2 = eval(input('Enter Second Point (x, y): '))
x3, y3 = eval(input('Enter Third Point (x, y): '))
# d = sqrt( ( x2 - x1 ) ^ 2 + ( y2 - y1 ) ^ 2 )
side1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
side2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print('')
print('Using the points : \n', x1, ',', y1, '\n', x2, ',', y2, '\n', x3, ',', y3)
print('')
print('The area of the triangle is', int(area * 100) / 100.0)
