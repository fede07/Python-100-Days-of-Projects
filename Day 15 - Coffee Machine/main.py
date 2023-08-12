from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "chocomilk":{
        "ingredients": {
            "milk": 150
        },
        "cost": 2.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
    

def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")
    return

def checkResource(resource, amount):
    total = resources[resource] - amount
    if(total < 0):
        print(f"Sorry, there's not enough {resource}.")
        return False
    else:
        return True
    
def updateResource(resource, ammout):
    resources[resource] = resources[resource] - ammout

def checkMenuPrice(selection, wallet):
    price = MENU[selection]["cost"]
    if(wallet < price):
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True
    
def changeBack(wallet, selection):
    price = MENU[selection]["cost"]
    global money
    money += price
    return wallet - price

def charge(selection):

    wallet = 0.0
    print("Please insert coins.")
    wallet += float(input("how many quarters?: ")) * 0.25
    wallet += float(input("how many dimes?: ")) * 0.10
    wallet += float(input("how many nickles?: ")) * 0.05
    wallet += float(input("how many pennies?: ")) * 0.01

    if not checkMenuPrice(selection, wallet):
        return False

    change = changeBack(wallet, selection)
    print(f"Here is ${change} in change.")

    return True

def serve(selection):
    
    empty = False

    for ingredient in MENU[selection]['ingredients']:
        amount = MENU[selection]["ingredients"][ingredient]
        if not checkResource(ingredient, amount):
            return False
    
    for ingredient in MENU[selection]['ingredients']:
        amount = MENU[selection]["ingredients"][ingredient]
        updateResource(ingredient, amount)

    print(f"Here is your {selection}. Enjoy!")

    return True

def clrScrn():
    system('cls')

def main():

    clrScrn()
    turnOn = True
    while(turnOn):
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection == "report":
            report()
        elif selection in MENU:
            if charge(selection):
                serve(selection)
        elif selection == "off":
            turnOn = False
        else:
            print("Sorry, could you repeat that?")

main()

