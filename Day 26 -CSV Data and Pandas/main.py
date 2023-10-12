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
print(weather_data["temp"])
