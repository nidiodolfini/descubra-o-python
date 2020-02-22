from math import floor
# 200 ml of water, 50 ml of milk, and 15 g
water = int(input('Write how many ml of water the coffee machine has: '))
milk = int(input('Write how many ml of milk the coffee machine has: '))
coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
amount_of_coffee = int(input('Write how many cups of coffee you will need: '))
water_necessary = floor(water / 200)
milk_necessary = floor(milk / 50)
coffee_beans_necessary = floor(coffee_beans / 15)
smallest_item = min(water_necessary, milk_necessary, coffee_beans_necessary)
if amount_of_coffee == smallest_item:
    print('Yes, I can make that amount of coffee')
elif amount_of_coffee < smallest_item:
    sobra = smallest_item - amount_of_coffee
    print(f"Yes, I can make that amount of coffee (and even {sobra} more than that)")
elif amount_of_coffee > smallest_item:
    sobra = -(smallest_item - amount_of_coffee)
    print(f"No, I can make only {-(sobra - amount_of_coffee)} cups of coffee")
