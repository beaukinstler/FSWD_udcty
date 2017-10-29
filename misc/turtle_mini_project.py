#This program draws a triangle of triangles

import turtle
import time
import math

window = turtle.Screen()
def create_triad(someturtle):
    someturtle.setheading(0)
    t = someturtle.clone()
    
    t1 = t.clone()
    t1.forward(20)

    t2 = t1.clone()
    t2.left(120)
    t2.forward(20)

bob = turtle.Turtle()
bob.penup()   
bob.pen(fillcolor="green",pencolor="blue")
bob.shape("triangle")
bob.shapesize(outline=1)
bob.tilt(-30)
bob.setpos(-200,-200)
counter = 7
current_heading = 60
while counter > 1:
    for _ in range(counter):
        bob.setheading(current_heading)
        bob.forward(40)
        create_triad(bob)
    counter -= 1
    current_heading -= 120



# click to exit
window.exitonclick()



