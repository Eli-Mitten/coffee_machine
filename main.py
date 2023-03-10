from db import MENU, resources

coffee_machine_is = True
money = 0


def show_report():
    global money
    print("__________REPORT__________")
    for k, v in resources.items():
        print(f"    {k}:{v}")
    print(f"    money: ${money}")
    print("__________END__________")


def check_resources(_selection_):
    r = resources
    i = MENU[_selection_]["ingredients"]
    for key, value in i.items():
        if value >= r[key]:
            print(f"Sorry there is not enough {key}, left {r[key]}, you need {value}")
            return False
    return True


def give_me_the_money():
    
    total = int(input("Who many quarters?: ")) * 0.25
    total += int(input("Who many dimes?: ")) * 0.10
    total += int(input("Who many nickel: ")) * 0.05
    total += int(input("Who many pennies?: ")) * 0.01
    print(f"Total inserted: $ {round(total, 2)}")
    return round(total, 2)


def is_money_enough(amount, selected_product):
    if not amount >= MENU[selected_product]['cost']:
        print(f"Importe insuficinete, return {amount}")
        return False
    else:
        print("Importe correcto")
        return True


def save_the_money(_amount, product_price):
    global money
    money += product_price
    print(f"Return: iserted money {_amount} - product price {product_price} = ${round(_amount - product_price)}")
    show_report()


def delete_product_from_resources(selected_product):
    products_ingredients = MENU[selected_product]["ingredients"]

    for key, value in products_ingredients.items():
        resources[key] -= value


def make_coffee(_selection):
    global money
    product_cost = MENU[_selection]['cost']

    # Check if there are enough resources
    if not check_resources(_selection):
        return

    # Show the selection price
    print(f"You selected {_selection}, please inset ${product_cost}")

    # Give me the f**ing money
    total_amount = give_me_the_money()
    if not is_money_enough(total_amount, _selection):
        return
    delete_product_from_resources(_selection)
    save_the_money(total_amount, product_cost)
    print(f"Enjoy your {_selection}!!")


while coffee_machine_is:
    selection = input("What would you like? (espresso/latte/cappuccino) admin: (report/off):")
    if selection == 'report':
        show_report()
    elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        make_coffee(selection)
    elif selection == 'off':
        coffee_machine_is = False
        print("Switch off")
    else:
        print("Wrong selection")
