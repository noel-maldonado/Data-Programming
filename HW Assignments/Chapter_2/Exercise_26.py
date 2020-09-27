#(Turtle: draw a circle) Write a program that prompts the user to enter the
#center and radius of a circle, and then displays the circle and its area, as shown
#in Figure 2.5.

import turtle
import math

radius = eval(input("Enter the radius: "))
x = eval(input("x-coordinate: "))
y = eval(input("y-coordinate: "))
area = math.pi * radius ** 2
area = int(radius * 100) / 100
t = turtle.Turtle()
t.penup()
t.goto(x, y - radius)
t.write(area)
t.pendown()
t.circle(radius)
turtle.done()