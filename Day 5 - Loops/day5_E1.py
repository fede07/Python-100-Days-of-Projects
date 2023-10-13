# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
student_heights_int = []
for n in range(0, len(student_heights)):
  student_heights_int[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0
cant = 0

for student_h in student_heights_int:
    total += student_h
    cant+=1

average = round(total/cant)

print(f"total height = {total}")
print(f"number of students = {cant}")
print(f"average height = {average}")
