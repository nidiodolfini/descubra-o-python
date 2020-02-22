money = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
if chicken <= money < goat:
    print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
elif goat <= money < pig:
    print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
    # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
elif pig <= money < cow:
    print(f'{round(money / pig - 0.5)} pigs' if round(money / pig - 0.5) > 1 else '1 pig')
    # print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
    # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
elif cow <= money < sheep:
    print(f'{round(money / cow - 0.5)} cows' if round(money / cow - 0.5) > 1 else '1 cow')
    # print(f'{round(money / pig - 0.5)} pigs' if round(money / pig - 0.5) > 1 else '1 pig')
    # print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
    # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
elif money >= sheep:
    print(f'{round(money / sheep - 0.5)} sheep' if round(money / cow - 0.5) > 1 else '1 sheep')
    # print(f'{round(money / cow - 0.5)} cows' if round(money / cow - 0.5) > 1 else '1 cow')
    # print(f'{round(money / pig - 0.5)} pigs' if round(money / pig - 0.5) > 1 else '1 pig')
    # print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
    # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')

else:
    print('None')




# word = float(input())
# if word < 2:
#     print("Analytic")
# elif 2 <= word <= 3:
#     print("Synthetic")
# else:
#     print("Polysynthetic")



# age = int(input())
# if age <= 16:
#     print("Lion King")
# elif 15 < age < 26:
#     print("Trainspotting")
# elif 25 < age < 41:
#     print("Matrix")
# elif 40 < age < 61:
#     print("Pulp Fiction")
# else:
#     print("Breakfast at Tiffany's")


# x = 99999
# print(x * 3) if x <= 99988 else print(x * 2)

# if answer == "yes":
#     print("Let's drink cocoa!")
# else:
#     print("I'd recommend a coffee!")


# a = int(input())asd
# b = int(input())
# if a > b:
#     print(a)
#     print(b)
# else:
#     print(b)
#     print(a)2


# word = input()
# dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
# if word in dictionary:
#     print('Correct')
# else:
#     print('Incorrect')
#

# sun = False
# print("It’s a day now!" if sun else "It’s a night for sure!")
#


# coin = False
#
# if coin:
#     print("Welcome to Charon's boat!")
# print('There is no turning back.')
#
#


# pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# omelette = "egg, milk, bacon, tomato, salt, pepper"
#
# ingredient = input()
# if ingredient in pasta:
#     print('You can make pasta')
# if ingredient in apple_pie:
#     print('You can make apple pie')
# if ingredient in ratatouille:
#     print('You can make ratatouille')
# if ingredient in chocolate_cake:
#     print('You can make chocolate cake')
# if ingredient in omelette:
#     print('You can make omelette')


# amount_of_coffee = int(input("Write how many cups of coffee you will need: "))
# print(f'For {amount_of_coffee} cups of coffee you will need:')
# print(f'{amount_of_coffee * 200} ml of water')
# print(f'{amount_of_coffee * 50} ml of milk')
# print(f'{amount_of_coffee * 15} g of coffee beans')

# a = True
# b = False
# c = a and not b
#
# print(a and (not c or b))
#
# print(not None or 1)


# Write how many cups of coffee you will need: > 25
# For 25 cups of coffee you will need:
# 5000 ml of water
# 1250 ml of milk
# 375 g of coffee beans


# set_number = 6557
# one = int(input())
# two = int(input())
# print((one + two) == set_number)


# To sum up, there is a list of priorities for all considered operations:
#
# parentheses ()
# power **
# unary minus - ()
# multiplication, division, and remainder * / %
# addition and subtraction + -
# from math import ceil
# # Read an integer:
# a = int(input())
# b = int(input())
# c = int(input())
# # Math
#
# classa=ceil(a/2)
# classb=ceil(b/2)
# classc=ceil(c/2)
# classall=(classa+classb+classc)
#
# print("%s" % classall)
#
# a=int(input())
# b=int(input())
# c=int(input())
# print((a//2)+(b//2)+(c//2)+(a%2)+(b%2)+(c%2))
