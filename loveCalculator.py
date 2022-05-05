import random
while (True):
    print("\nEnter your choice: ")
    print("\t1. Paper")
    print("\t2. Scisior")
    print("\t3. Rock")
    print("\t4. To Quit")
    ch1 = int(input("  Enter choice: "))
    comp = random.randint(1, 3)
    print("Computer Choice", comp)
    if ch1 == comp:
        print("!! TIE !!")
    elif ch1 == 1:
        # print(ch1)
        if comp == 2:
            print("Computer WON")
        elif comp == 3:
            print("You WON")
    elif ch1 == 2:
        # print(ch1)
        if comp == 1:
            print("You WON")
        elif comp == 3:
            print("Computer WON")
    elif ch1 == 3:
        # print(ch1)
        if comp == 1:
            print("You WON")
        elif comp == 2:
            print("Computer WON")
    elif ch1 == 4:
        break
    else:
        print("!! Enter correct choice !!")
    print("\n\n")
