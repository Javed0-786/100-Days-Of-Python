import random
name = input("Enter the name of persons separated by Commas: ")
list = name.split(", ")
print(list[random.randint(0, len(list)-1)])
print(random.choice(list))
