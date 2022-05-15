import random

num = random.randint(1, 100)
print("number is: ", num)
print("You have to guess a number between 1 and 100")
check = 1
ch = int(input("Enter 1 for easy level or 2 for difficult one: "))
if (ch == 1):
    for i in range(10):
        print("You have ", 10-i, " attempts left ")
        inp = int(input("Enter number: "))
        if (inp == num):
            print("You got it right")
            print("Your score: ", 9-i)
            check = 0
            break

        elif (inp > num):
            print("Too high")

        elif (inp < num):
            print("Too low")

        if (i == 9 and check == 1):
            print("You lost")


elif (ch == 2):
    for i in range(5):
        print("You have ", 5-i, " attempts left ")
        inp = int(input("Enter number: "))
        if (inp == num):
            print("You got it right")
            print("Your score: ", 4-i)
            check = 0
            break

        elif (inp > num):
            print("Too high")

        elif (inp < num):
            print("Too low")

        if (i == 4 and check == 1):
            print("You lost")


else:
    print("wrong choice")
