# import pandas

# data = pandas.read_csv("squirrel data.csv")
# # print(data["Primary Fur Color"])
# list_data = data["Primary Fur Color"].to_list()
# # print(list_data)
# # print(type(list_data))

# gray_count = 0
# black_count = 0
# cinnamon_count = 0
# nan_count = 0
# for color in list_data:
#     if color == "Gray":
#         gray_count += 1

#     elif color == "Cinnamon":
#         cinnamon_count += 1

#     elif color == "Black":
#         black_count += 1

#     else:
#         nan_count += 1

# new_data = {
#     "Fur Color": ["gray", "black", "cinnamon", "nan"],
#     "count": [gray_count, black_count, cinnamon_count, nan_count]
# }

# my_data = pandas.DataFrame(new_data)
# my_data.to_csv("data.csv")

# print(gray_count, cinnamon_count, black_count, nan_count)


import pandas

data = pandas.read_csv("squirrel data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_count)
print(black_count)
print(cinnamon_count)
print(data[data["Primary Fur Color"] == "Gray"])

# new_data = {
#     "Fur Color": ["gray", "black", "cinnamon"],
#     "Count": [gray_count, black_count, cinnamon_count]
# }

# df = pandas.DataFrame(new_data)
# df.to_csv("squirrel_color_count.csv")
