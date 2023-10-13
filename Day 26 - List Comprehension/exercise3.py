with open("file1.txt") as file1:
  contents1 = file1.readlines()
  print(contents1)
with open("file2.txt") as file2:
  contents2 = file2.readlines()

list_1 = [int(number.strip()) for number in contents1]
list_2 = [int(number.strip()) for number in contents2]

result = []

print(list_1)
print(list_2)

for number in list_1:
  if number in list_2:
    result.append(number)

# Write your code above 👆
print(result)