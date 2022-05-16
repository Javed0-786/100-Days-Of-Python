MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

while (True):
    check = 0
    type = input("What would you like? (espresso/latte/cappuccino): ")

    if type == 'off':
        quit()
    elif type == 'report':
        for name, item in resources.items():
            print(f"{name} : {item}")

    else:
        rpW = resources['water']
        rpM = resources['milk']
        rpC = resources['coffee']

        mpW = MENU[type]['ingredients']['water']
        mpM = MENU[type]['ingredients']['milk']
        mpC = MENU[type]['ingredients']['coffee']

        for product in MENU[type]['ingredients']:
            if (rpW < mpW and product == 'water'):
                print(f'\tSorry there is not enough {product} 🚰')
                check = 0

            elif (rpM < mpM and product == 'milk'):
                print(f'\tSorry there is not enough {product} 🥛')
                check = 0

            elif (rpC < mpC and product == 'coffee'):
                print(f'\tSorry there is not enough {product} ☕')
                check = 0

            elif (rpW >= mpW and rpM >= mpM and rpC >= mpC):
                # resources[product] -= MENU[type]['ingredients'][product]
                check = 1

        if (check == 1):
            print(f'\n\tYour {type} coffee is available 💖')
            print(f'\tPlease proceed for the payment\n')
            print("\nPlease enter the Coins: ")
            quart = int(input("\tQuarters: "))
            dimes = int(input("\tDimes: "))
            nickles = int(input("\tNickles: "))
            pennies = int(input("\tPennies: "))
            mC = MENU[type]['cost']
            cC = 0.25 * quart + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
            print(cC)
            if (mC <= cC):
                print(f'Your change is: {round(cC-mC, 2)}')
                print("\t🍵🍵🍵🍵🍵🍵🍵🍵🍵🍵🍵🍵")
                print(f"\tHere is your {type}. Enjoy 💖")
                resources['money'] += mC
                for product in MENU[type]['ingredients']:
                    resources[product] -= MENU[type]['ingredients'][product]

            else:
                print("Sorry that's not enough money. Money refunded.")
                print("\t\t💵💶🏧💰")

        else:
            print("\nPlease try for something else 🍵")
