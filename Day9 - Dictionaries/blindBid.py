from art import logo
from os import system

def printLogo():
    print(logo)

printLogo()
print("Welcome to the secret auction.")
name = input("What is your name? ")
bid = int(input("What's your bid? $"))

bidders = {
    name: bid
}

answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

while(answer != "yes" and answer != "no"):
    answer = input("I'm sorry, are there any other bidders? Type 'yes' or 'no': ").lower()

if(answer == "yes"):
    while(answer == "yes"):
        system('cls')
        name = input("What is your name? ")
        bid = int(input("What's your bid? $"))
        bidders[name] = bid
        answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        while(answer != "yes" and answer != "no"):
            answer = input("I'm sorry, are there any other bidders? Type 'yes' or 'no': ").lower()

winner = ""
topbid = 0

for bidder in bidders:
    if bidders[bidder] > topbid:
        winner = bidder
        topbid = bidders[bidder]

system('cls')
print(f"The winner is {winner} with ${topbid}")
