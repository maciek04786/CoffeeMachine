MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money = {
    'quarters' : 0.25,
    'dimes' : 0.10,
    'nickles' : 0.05,
    'pennies' : 0.01
}

def deduct_resources(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]

def check_resources(drink):
    for item in resources:
        return item if resources[item] <= MENU[drink]["ingredients"][item] else False

def check_pay():
    full_amount = 0
    print("Please insert coins.")
    n1 = int(input("How many quarters? "))
    n2 = int(input("How many dimes? "))
    n3 = int(input("How many nickles? "))
    n4 = int(input("How many pennies? "))
    full_amount = float(n1 * money['quarters'] +
                        n2 * money['dimes'] +
                        n3 * money['nickles'] +
                        n4 * money['pennies'])
    return full_amount

def main():
    customer_money = 0
    order = ''
    
    while order != "off":
        order = input("What drink would you like? (espresso/latte/cappuccino?): ")
        if order == "report":
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${customer_money:.2f}')
        elif check_resources(order):
            print(f"Sorry, there's not enough {check_resources(order)}")
        else:
            check = check_pay()
            if check == MENU[order]["cost"]:
                deduct_resources(order)
                customer_money += check
                print("Here is your latte ☕ Enjoy!")
            elif check > MENU[order]["cost"]:
                print(f'Here is ${check - MENU[order]["cost"]:.2f} in change.')
                deduct_resources(order)
                customer_money += MENU[order]["cost"]
                print("Here is your latte ☕ Enjoy!")
            elif check < MENU[order]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
                break

main()
