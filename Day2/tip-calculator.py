#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
total = float(total)
percent = input("What percentage tip wouldyou like to give? 10, 12 or 15? ")
percent = float(percent)
percent = percent/100 + 1
people = input("How many people to split the bill? ")
people = int(people)

pay = (total / people) * percent
pay = round(pay, 2)
pay = "{:.2f}".format(pay)

print(f"Each person should pay: ${pay}")

