# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#Write your code below this line 👇

years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")