money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9
action = ''


def machine_has():
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{coffee_beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def use_resource(water1, milk1, coffee_beans1, cup):
    global water
    global milk
    global coffee_beans
    global cups
    global money
    if water1 > water:
        print('Sorry, not enough water!')
    elif milk1 > milk:
        print('Sorry, not enough milk!')
    elif coffee_beans1 > coffee_beans:
        print('Sorry, not enough Coffee Beans!')
    elif cup > cups:
        print('Sorry, not enough cup!')
    else:
        water -= water1
        milk -= milk1
        coffee_beans -= coffee_beans1
        cups -= cup
        print('I have enough resources, making you a coffee!')


def buy():
    global money
    action = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if action == '1':
        use_resource(250, 0, 16, 1)
        money += 4
    elif action == '2':
        use_resource(350, 75, 20, 1)
        money += 7
    elif action == '3':
        use_resource(200, 100, 12, 1)
        money += 6
    elif action.lower() == 'back':
        machine_action()
    print()


def fill():
    global water
    global milk
    global coffee_beans
    global cups
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    coffee_beans += int(input('Write how many grams of coffee beans do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee do you want to add: '))
    print()


def take():
    global money
    print(f'I gave you ${money}')
    money = 0
    print()


def machine_action():
    global action
    while action.lower() != 'exit':
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action.lower() == 'exit':
            break
        elif action.lower() == 'fill':
            fill()
        elif action.lower() == 'take':
            take()
        elif action.lower() == 'remaining':
            print()
            machine_has()
            machine_action()
        elif action.lower() == 'buy':
            buy()
    print()


machine_action()
