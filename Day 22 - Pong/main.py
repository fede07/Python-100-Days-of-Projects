from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(350)
paddle_l = Paddle(-350)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")

screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

player1Score = 0
player2Score = 0

gameIsOn = True

while(gameIsOn):
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    #Detect collision with walls
    if ball.ycor() > 270 or ball.ycor() <-270:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320: 
        ball.bounce_x()
    
    #Detect score

    if ball.xcor() > 380:
        ball.reset_score()
        scoreboard.increase_score_l()
    elif ball.xcor() < -380:
        ball.reset_score()
        scoreboard.increase_score_r()


screen.exitonclick()