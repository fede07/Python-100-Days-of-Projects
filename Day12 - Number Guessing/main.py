#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from os import system
import random

secret_number = random.randint(1, 100)

system('cls')
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"(The number is {secret_number})")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
lives = 0

if difficulty == "easy":
    lives = 10
else:
    lives = 5

isOver = False

while not isOver:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if(guess == secret_number):
        print(f"You got it! the answer was {secret_number}")
        isOver = True
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Too low.")

    lives-=1

    if(lives == 0):
        isOver = True 

    if(not isOver and lives > 0):
        print("Guess again.")
    elif lives == 0:
        print("You've run out of guesses, you lose")




