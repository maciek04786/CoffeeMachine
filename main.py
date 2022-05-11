MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

money = 0


def deduct_resources(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]


def check_resources(drink):
    for item in resources:
        if resources[item] >= MENU[drink]["ingredients"][item]:
            return "yes"
        else:
            return item


def check_pay(drink):
    full_amount = 0
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    print("Please insert coins.")
    n1 = int(input("How many quarters? "))
    n2 = int(input("How many dimes? "))
    n3 = int(input("How many nickles? "))
    n4 = int(input("How many pennies? "))
    full_amount = float(n1 * quarters + n2 * dimes + n3 * nickles + n4 * pennies)
    return full_amount


def main():
    global money
    drink = input("What drink would you like? (espresso/latte/cappuccino?): ")
    if drink == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money:.2f}')
        main()
    elif drink == "off":
        exit()
    elif check_resources(drink) != "yes":
        print(f"Sorry, there's not enough {check_resources(drink)}")
        main()
    else:
        check = check_pay(drink)
        if check == MENU[drink]["cost"]:
            deduct_resources(drink)
            money += check
            print("Here is your latte ☕ Enjoy!")
            main()
        elif check > MENU[drink]["cost"]:
            print(f'Here is ${check - MENU[drink]["cost"]:.2f} in change.')
            deduct_resources(drink)
            money += MENU[drink]["cost"]
            print("Here is your latte ☕ Enjoy!")
            main()
        elif check < MENU[drink]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")


main()