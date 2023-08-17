#Run from same folder as this file
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract(".\\image.jpg", 30) 

t.colormode(255)

turtle = t.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.shape("turtle")
turtle.speed(0)
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

dots = 100

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

def paintDots(size):
    for i in range(1, dots + 1):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)
        if i % 10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)

paintDots(10)

screen = t.Screen()
screen.exitonclick()


