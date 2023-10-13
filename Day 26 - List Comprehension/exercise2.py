list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:

list_of_numbers = [int(string_) for string_ in list_of_strings ]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"

result = [number for number in list_of_numbers if number%2 == 0]

# Write your code 👆 above:
print(result)