from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 56, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scoreLeft = 0
        self.scoreRight = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.write(f"{self.scoreLeft} | {self.scoreRight}", align=ALIGMENT, font=FONT) 
        self.hideturtle()

    def update_score(self):
        self.write(f"{self.scoreLeft} | {self.scoreRight}", align=ALIGMENT, font=FONT) 
   
    def increase_score_l(self):
        self.scoreLeft += 1
        self.clear()
        self.update_score()

    def increase_score_r(self):
        self.scoreRight += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGMENT, font= FONT)

