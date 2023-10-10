from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from os import system
import time

system("cls")
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True

# def game_over():
#     game_is_on = False
#     score.game_over()

def resetGame():
    score.reset()
    snake.reset()

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        resetGame()

    #detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            resetGame()
screen.exitonclick()