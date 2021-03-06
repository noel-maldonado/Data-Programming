# (Geometry: display angles) Rewrite Listing 2.9, ComputeDistance.py, using the
# following function for computing the distance between two points.
# def distance(x1, y1, x2, y2):
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))

a = distance(x2, y2, x3, y3)
b = distance(x1, y1, x3, y3)
c = distance(x1, y1, x2, y2)

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are", round(A, 2), round(B, 2), round(C, 2))
