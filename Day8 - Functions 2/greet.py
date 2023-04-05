# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
    print(f"Hello {name}\nHow do you do?\nIsn't the weather nice today?")

greet("Leon")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Leon", "USA")

greet_with(location="USA", name="Leon")