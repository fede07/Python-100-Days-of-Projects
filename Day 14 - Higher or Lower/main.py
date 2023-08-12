from art import logo, vs
from game_data import data
from os import system
import random

def getRandomEntry():
    """Gets a random entry from a dictionary"""
    key = random.choice(list(data))
    return key

def compare(guess, selection_a, selection_b):
    if guess == 'a' and selection_a >= selection_b:
        return True
    elif guess == 'b' and selection_b >= selection_a:
        return True
    else:
        return False

def clrScrn():
    system('cls')

def pLogo():
    print(logo)

def formatKey(key):
    name = key['name']
    description = key['description']
    country = key['country']
    follower_count = key['follower_count']
    return f"{name}, a {description} from {country}. \n(Followers: {follower_count})"

def printQuestion(optionA, optionB):
    print(f"Compare A: {formatKey(optionA)}")
    print(vs)
    print(f"\nAgainst B: {formatKey(optionB)}")
    return input("\nWho has more followers? Type 'A' or 'B': ").lower()


def main():
    isOver = False
    score = 0

    optionA = getRandomEntry()
    optionB = getRandomEntry()
    if optionA == optionB:
        optionB = getRandomEntry()

    while not isOver:
        clrScrn()
        pLogo()
        
        if(score > 0):
            print(f"You are right! Current score: {score}")

        guess = printQuestion(optionA, optionB)
        result = compare(guess, optionA['follower_count'], optionB['follower_count'])
        
        if result == True:
            score+=1
            optionA = optionB
            optionB = getRandomEntry()
        else:
            isOver = True
    
    clrScrn()
    pLogo()
    print(f"Sorry, that's wrong. Final Score: {score}")

main()