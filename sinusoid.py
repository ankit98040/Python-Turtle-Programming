import turtle
import math
import random

a = turtle.Turtle()
turtle.colormode(255)
a.speed(25)

for i in range(2000):
	a.forward(10)
	a.left(math.sin(i/10)*25)
	a.left(20)

turtle.done()