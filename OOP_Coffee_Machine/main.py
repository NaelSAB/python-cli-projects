from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


latte = MenuItem("latte", 200, 150, 24, 2.0)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
Is_machine_ON = True

while(Is_machine_ON):
    order = input(f"what's your order? {menu.get_items()} ").lower()
    if order == "report":
        coffee_machine.report()
        money.report()
    elif order == "off":
        Is_machine_ON = False
    else:
        item = menu.find_drink(order)
        if (not item):
            continue
        elif (coffee_machine.is_resource_sufficient(item)):
            Is_Accepted = money.make_payment(item.cost)
            if (Is_Accepted):
                coffee_machine.make_coffee(item)