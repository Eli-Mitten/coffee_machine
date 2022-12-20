from db import MENU, resources, money

coffee_machine_is = True


def check_resources(_selection_):
    r = resources
    i = MENU[_selection_]["ingredients"]
    for key, value in i.items():
        if value >= r[key]:
            print(f"Sorry there is not enough {key}, left {value}")
            return False
    return True


def give_me_de_money():
    total = 0
    # coger el dinero del usuario
    money = input("Insert")
    # calcular cuanto es en total

    return total


def make_coffee(_selection):
    # Check if there are enough resources
    if not check_resources(_selection):
        return
    else:
        print("Recursos suficientes en la maquina")
    # Show the selection price
    print(f"You selected {_selection}, please inset ${MENU[_selection]['cost']}")
    # Give me the f**ing money
    give_me_de_money()

    print("Todo ok")


while coffee_machine_is:
    selection = input("What would you like? (espresso/latte/cappuccino):")
    if selection == 'report':
        for k, v in resources.items():
            print(f"{k}: {v}")
        print(f"money: ${money}")
    elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        make_coffee(selection)
    elif selection == 'off':
        coffee_machine_is = False
        print("Switch off")
