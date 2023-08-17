import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

turtle = t.Turtle()
turtle.shape("turtle")
turtle.speed(0)
turtle.pensize(9)

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

for _ in range(200):
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
    turtle.color(random_color())

screen = t.Screen()
screen.exitonclick()