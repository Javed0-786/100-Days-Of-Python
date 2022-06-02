# import csv
# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     i = 0
#     for row in data:
#         print(row)
#         if i != 0:
#             temperature.append(int(row[1]))
#         i += 1
#     print(temperature)


import pandas

# data = pandas.read_csv("weather-data.csv")

# print(data["temp"])
# print(type(data))

# temperature = data["temp"].to_list()
# avg = sum(temperature)/len(temperature)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])


# my_dict = {
#     'student': ['javed', 'raju', 'mohit', 'sunil'],
#     'marks': [24, 35, 37, 45]
# }

# my_data = pandas.DataFrame(my_dict)
# my_data.to_csv("new_data.csv")

# data = pandas.read_csv("new_data.csv")
# print(data)


# Primary fur color with only three possible values
# count the number of squarrels on the basis of colors
