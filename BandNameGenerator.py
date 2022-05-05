print("\tBand Name Generator\n")
while (True):
    print("1. City and Dog\n2. Girlfriend and Dog\n3. City and Girlfreind\n4. To Exit")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        city = input("Enter city name: ")
        dog = input("Enter dog name: ")
        print("\aBand name is: ", city + dog)

    elif choice == 2:
        GF = input("Enter girlfriend name: ")
        dog = input("Enter dog name: ")
        print("\aBand name is: ", GF + dog)

    elif choice == 3:
        city = input("Enter city name: ")
        GF = input("Enter girlfriend name: ")
        print("\aBand name is: ", city + GF)

    elif choice == 4:
        break

    else:
        print("\a\aPlease Enter correct Choice")

    print("\n\n")
