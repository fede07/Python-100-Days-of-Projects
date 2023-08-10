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

SECRET_NUMBER = random.randint(1, 100)
EASY = 10
HARD = 5

def setDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY
    else:
        return HARD
    
def checkAnswer(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You've got it! The answe was {answer}.")
        return True

def game():
    system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"(The number is {SECRET_NUMBER})")

    lives = setDifficulty()
    isOver = False

    while not isOver:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        isOver = checkAnswer(guess, SECRET_NUMBER)
        lives-=1

        if(lives == 0):
            isOver = True 

        if(not isOver and lives > 0):
            print("Guess again.")
        elif lives == 0:
            print("You've run out of guesses, you lose")

game()




