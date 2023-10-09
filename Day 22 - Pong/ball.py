from turtle import Turtle

STARTING_SPEED = 0.1

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("square")        
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.moveSpeed = STARTING_SPEED

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def bounce_y(self):
        self.ymove *= -1
        self.moveSpeed *= 0.9

    def bounce_x(self):
        self.xmove *= -1

    def reset_score(self):
         self.goto(0,0)
         self.xmove *= -1
         self.moveSpeed = STARTING_SPEED