
numbers = [1, 2, 3]

numbers_list = [n+1 for n in numbers]

print(numbers_list)

name = "Angela"

name_list = [letter for letter in name]

print(name_list)

range_list = [number*2 for number in range(1, 5)]

print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]

long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)