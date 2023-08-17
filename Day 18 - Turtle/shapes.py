from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(sides):
    if sides <= 0:
        return
    angle_current = (360/sides)
    for _ in range(0, sides):
        turtle.forward(100)
        turtle.right(angle_current)

turtle = Turtle()
turtle.shape("turtle")

# turtle.color(color)
# for _ in range(0, 4):
#     for _ in range(0,10):
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()
#     turtle.right(90)

for sides in range(3, 15):
    turtle.color(random.choice(colours))
    draw_shape(sides)
    
screen = Screen()
screen.exitonclick()