from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = int(0)
        self.highscore = int(0)
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align=ALIGMENT, font=FONT) 
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align=ALIGMENT, font=FONT) 
   
    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGMENT, font= FONT)

    def loadScores(self):
        with open("data.txt", mode="r") as file:
            self.highscore = file.read()
    
    def saveScores(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))   
            
    def reset(self) -> None:
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.saveScores()
        self.score = 0
        self.update_score()