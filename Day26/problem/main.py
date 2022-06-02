# list = [i for i in range(1, 5)]
# new_list = [i*2 for i in list]
# print(new_list)

# names = ["rohit", "raman", "rajesh", "raju", "ram",
#          "raj", "rajiv", "ramnath", "rahul", "rohan", "ronit"]

# new_names = [name.upper() for name in names if len(name) > 5]
# print(new_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_number = [number**2 for number in numbers]
# print(squared_number)

# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)


# Write your code above 👆
with open("file1.txt") as fp:
    list1 = fp.readlines()
    list1 = [int(item.strip()) for item in list1]

with open("file2.txt") as fp2:
    list2 = fp2.readlines()
    list2 = [int(item.strip()) for item in list2]

print([item for item in list1 if item in list2])
