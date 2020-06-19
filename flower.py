import turtle
turtle.color("red","yellow")
turtle.begin_fill() #for filling the closed surface

turtle.speed(10) # for controlling turtle speed

for i in range(50):
    turtle.forward(300)
    turtle.left(170)

turtle.end_fill()  #ending the fill method

turtle.done()
