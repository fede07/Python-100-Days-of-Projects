from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system


def clrScrn():
    system("cls")

def main():

    menu = Menu()
    coffeeM = CoffeeMaker()
    moneyM = MoneyMachine()
    isOn = True
    clrScrn()
    while(isOn):


        selection = input(f"What would you like? ({menu.get_items()}): ").lower()

        if selection == "report":
            coffeeM.report()
            moneyM.report()
        elif selection == "off":
            isOn = False
        else:
            item = menu.find_drink(selection)
            paid = False

            if item and item.name != "null" and coffeeM.is_resource_sufficient(item):
                paid = moneyM.make_payment(cost=item.cost)
            if paid:
                coffeeM.make_coffee(order=item)


    return


main()