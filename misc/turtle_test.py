import turtle
import time
import math


def draw_square(some_turtle):
    some_turtle.shape("circle")
    some_turtle.color("blue")
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
        #time.sleep(1)


def draw_circle():
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.circle(40)

def draw_triange(some_turtle,side_length):
    some_turtle.color("green")
    for i in range(3):
        some_turtle.forward(side_length)
        some_turtle.right(120)


def draw_pattern(some_turtle):
    heading = 360
    while (heading >= 0):
        some_turtle.setheading(heading)
        draw_square(some_turtle)
        heading -= 2

def draw_shrinking_pattern(some_turtle,heading, length, divisor):
    counter = 10
    some_turtle.setheading(heading)
    while (counter > 0):
        direction = 90
        some_turtle.forward(length)
        draw_triange(some_turtle, length )
        some_turtle.right(direction + ((1+math.sqrt(5))/2))
        length = length +((1+math.sqrt(5))/2)
        newTurtle = turtle.Turtle()
        newTurtle.setpos(some_turtle.pos())
        newTurtle.setheading(some_turtle.heading())
        newTurtle.right(direction + ((1+math.sqrt(5))/2))
        newTurtle.forward(length*(1+math.sqrt(5))/2)      
        counter -= 1
        draw_shrinking_pattern(newTurtle,newTurtle.heading(),length + (1+math.sqrt(5))/2,divisor)


    

def make_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # brad = turtle.Turtle()
    # #draw_pattern(brad)
    # #draw_square(brad)

    liz = turtle.Turtle()
    liz.color("green")
    #draw_circle()
    #draw_triange(liz, 100)
    draw_shrinking_pattern(liz,90,50,4)
    window.exitonclick()

make_art()

