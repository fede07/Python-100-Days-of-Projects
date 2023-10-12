# with open(r"Day 26 -CSV Data and Pandas\weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open(r"Day 26 -CSV Data and Pandas\weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

weather_data = pandas.read_csv("Day 26 -CSV Data and Pandas\weather_data.csv")
# print(weather_data["temp"])

data_dict = weather_data.to_dict()
print(data_dict)

temp_list = weather_data["temp"].to_list()
print(temp_list)

# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
# average_temp = round(temp_sum / len(temp_list))
# print(f"Average temp: {average_temp}")

# average_temp = round(weather_data["temp"].mean())
# print(f"Average temp: {average_temp}")

# max_temp = weather_data["temp"].max()

# print(f"Max Value: {max_temp}")

# print(weather_data[weather_data.day == "Monday"])

# monday_data = weather_data[weather_data.day == "Monday"]
# monday_temp = monday_data.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#create data frame

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv(r"Day 26 -CSV Data and Pandas\students.csv")