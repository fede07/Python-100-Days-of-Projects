rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

import random

choices = [rock, paper, scissors]
bandera = True
 
while(bandera):
    choice = int(input("Rock, paper, scissors!? "))
    if(choice == 0 or choice == 1 or choice == 2):
        bandera = False
    
bot = random.randint(0,2)

print(f"Your choice:\n{choices[choice]} ")
print(f"Computer chose:\n {choices[bot]}")

if(choice == bot):
    print("Draw!")
else:
    match choice:
        case 0: 
            if(bot == 1):
                print("You lose")
            else:
                print("You win!")
        case 1:
            if(bot == 2):
                print("You lose")
            else:
                print("You win!")
        case 2:
            if(bot == 0):
                print("You lose")
            else:
                print("You win!")
