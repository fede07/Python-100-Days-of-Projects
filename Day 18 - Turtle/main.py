from turtle import Turtle, Screen


turtle = Turtle()
turtle.shape("turtle")
color = 0
# turtle.color(color)
# for _ in range(0, 4):
#     for _ in range(0,10):
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()
#     turtle.right(90)

angle = 90

for i in range(3, 7):
    for j in range(3, i):
        angle_current = angle / j
        turtle.forward(100)
        turtle.right(angle_current)

screen = Screen()
screen.exitonclick()