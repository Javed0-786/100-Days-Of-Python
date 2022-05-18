from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = CoffeeMaker()
menu = Menu()
finance = MoneyMachine()


while True:

    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        quit()

    elif choice == 'report':
        order.report()
        finance.report()

    elif choice in menu.get_items():
        coffee = menu.find_drink(choice)
        check = order.is_resource_sufficient(coffee)
        if check == True:
            print("Your coffee is available, Please proceed for payment.")
            cost = coffee.cost
            payment = finance.make_payment(cost)
            if payment == True:
                order.make_coffee(coffee)

    else:
        print("Invalid Input")
