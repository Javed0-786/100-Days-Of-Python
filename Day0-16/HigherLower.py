import random
from GameData import data


# approach

# generate a random item from the list

# print the values and description of the previous one
# print the discription of the random
# compare the random with the previous
# if random is higher than previous continue else quit
l = len(data)
pre = data[0]
score = 0

while (True):
    r = random.randint(0, 49)
    new = data[r]
    for key, value in pre.items():
        print(f'{key} : {value}')

    print("V/S")

    for key, value in new.items():
        if (key != 'follower_count'):
            print(f'{key} : {value}')

    choice = input("Enter 'l' for lower and 'h' for higher: ")

    if (pre['follower_count'] <= new['follower_count'] and choice == 'h'):
        # higher
        score += 1

    elif(pre['follower_count'] > new['follower_count'] and choice == 'l'):
        # lower
        score += 1

    else:
        print(f'score: {score}')
        quit()

    pre = new
    print("\n\n")
