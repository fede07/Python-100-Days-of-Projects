with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("test.txt", mode="w") as file:
#     file.write("Hello there")

with open("test.txt", mode="a") as file:
    file.write("\nYou opened this again")