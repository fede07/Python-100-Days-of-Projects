import turtle as t
import random

turtle = t.Turtle()
turtle.shape("turtle")
turtle.speed(0)
turtle.pensize(4)

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):
        if i % 2 == 0:
            turtle.color("red")
        else:
            turtle.color("blue")
        turtle.circle(100)
        turtle.left(size_of_gap)

spirograph(5)

screen = t.Screen()
screen.exitonclick()