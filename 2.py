from turtle import *

shape("turtle")
 
size=24
 
bgcolor("black")
 
pensize(3)
 
speed(400)
 
pu();home();fd(50);pd()
 
for i in range(size):
 	
 	rt(90);pencolor("red")
 	circle(60,360);fd(50);lt(10);fd(50);lt(10)
 	lt(120);pencolor("pink")
 	circle(90,360);fd(50);lt(10);fd(50);lt(10)
 	lt(120);pencolor("red")
 	circle(120,360);fd(50);lt(10);fd(50);lt(10)
 	pencolor("pink")
 	
 	circle(150);fd(50);lt(10);fd(50);lt(10)

pu();home();fd(-500);pd()

for i in range(size):
 	
 	rt(90);pencolor("green")
 	circle(60,360);fd(50);lt(10);fd(50);lt(10)
 	lt(120);pencolor("light green")
 	circle(90,360);fd(50);lt(10);fd(50);lt(10)
 	lt(120);pencolor("green")
 	circle(120,360);fd(50);lt(10);fd(50);lt(10)
 	pencolor("light green")
 	
 	circle(150);fd(50);lt(10);fd(50);lt(10)

pu();home();fd(600);pd()

for i in range(size):
 	
 	rt(90);pencolor("blue")
 	circle(60,360);fd(50);lt(10);fd(50);lt(10)
 	lt(120);pencolor("light blue")
 	circle(90,360);fd(50);lt(10);fd(50);lt(10)
 	lt(120);pencolor("blue")
 	circle(120,360);fd(50);lt(10);fd(50);lt(10)
 	pencolor("light blue")
 	circle(150);fd(50);lt(10);fd(50);lt(10)

exitonclick()