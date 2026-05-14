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
        "cost": 2.0,
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

coins = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}

income = 0.0

def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n Money: ${income} ")

def is_Resource_Avilable(menu):
    if (menu["ingredients"]["water"] <= resources["water"]):
        if (menu["ingredients"]["coffee"] <= resources["coffee"]):
            if ("milk" not in menu["ingredients"]):
                return True
            elif (menu["ingredients"]["milk"] <= resources["milk"]):
                return True
            else:
                print("milk isn't enough")
                return False
        else:
            print("Coffee isn't enough")
            return False
    else:
        print("Water isn't enough")
        return False

def calculate_coin(price):
    try:
        pennies = int(input("how manny pennies? "))
        nickles = int(input("how manny nickles? "))
        dimes = int(input("how manny dimes? "))
        quarters = int(input("how manny quarters? "))
        total = (pennies * coins["pennies"]) + (nickles * coins["nickles"]) + (dimes * coins["dimes"]) + (quarters * coins["quarters"])
        if (total == price):
            return True
        elif (total > price):
            print(f"Here is ${total - price:.2f} dollars in change.")
            return True
        else:
            print("Sorry, not enough. Money refunded.")
            return False
    except(ValueError):
        print("you input string! Please enter a number")
        return calculate_coin(price)

def income_increase(price):
    global income
    income += price

def resources_change(ingred):
    global resources
    resources["water"] -= ingred["water"]
    resources["coffee"] -= ingred["coffee"]
    if ("milk" in ingred):
        resources["milk"] -= ingred["milk"]

def The_Order(order):
    if order == "off":
        global Machine
        Machine = False
    elif order == "report":
        report()
    else:
        for list in MENU:
            if (list == order):
                is_enough = is_Resource_Avilable(MENU[list])
                if (is_enough):
                    ispay = calculate_coin(MENU[list]["cost"])
                    if (ispay):
                        income_increase(MENU[list]["cost"])
                        resources_change(MENU[list]["ingredients"])
                        print(f"Here is your {list}. Have fun!")


Machine = True

while Machine:
    user_Order = input("What's your order? (espresso/latte/cappuccino): ").lower()
    The_Order(user_Order)
