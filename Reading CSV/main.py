# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     data_list = []
#     for row in data:
#         data_list.append(row)
#
#     for row in data_list[1:]:
#         temperature.append(int(row[1]))
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_list = data["temp"].to_list()

# average = sum(data_list)/len(data_list)
# print(round(average))
# average = data["temp"].mean()
# maximum = data["temp"].max()
# print(data[data.temp == maximum])

monday = data[data.day == "Monday"]
temp = monday.temp
print(temp)
# data_dic = {
#     "students" : ["Amy", "James", "Nima"],
#     "scores" : [53, 65, 89]
# }

# new_data = pandas.DataFrame(data_dic)
# new_data.to_csv("new_data.csv")