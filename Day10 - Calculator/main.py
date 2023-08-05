#Calculator

from art import logo

#Add
def add(a, b):
    return a+b

#Substract
def substract(a, b):
    return a-b

#Multiply
def multiply(a, b):
    return a*b

#Divide
def divide(a, b):
    return a/b

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():

    print(logo)

    repeat = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
            print(symbol)

    while(repeat):

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:").lower()
        if(cont == "y"):
            num1 = answer
        else:
            repeat = False
        

    print("Goodbye!")

calculator()
