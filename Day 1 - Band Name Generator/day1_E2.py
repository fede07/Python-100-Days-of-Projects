def contarLetras(string):
    contador = 0
    for x in string:
        contador += 1 
    return contador

nombre = input("What is your name? ")
print(contarLetras(nombre))
