# 🚨 Don't change the code below 👇
from re import L
import string
from turtle import st


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

stringComb = name1 + name2
stringComb = stringComb.lower() 

t = stringComb.count("t")
r = stringComb.count("r")
u = stringComb.count("u")
e = stringComb.count("e")

true = t + r + u + e

l = stringComb.count("l")
o = stringComb.count("o")
v = stringComb.count("v")
e = stringComb.count("e")

love = l + o + v + e

score = int(f"{true}{love}")

if(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
elif(score <= 10 or score >= 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
else:
    print(f"Your score is {score}.")
