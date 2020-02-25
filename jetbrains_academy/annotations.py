x = float(input())
y = float(input())
if x < 0 and y < 0:
    print('III')
elif y < 0 and x > 0:
    print('IV')
elif x < 0 and y > 0:
    print('II')
elif x > 0 and y > 0:
    print('I')
else:
    print('(0, 0)')



# word = input() #taking a string from user & storing into variable.
# li = list(word) #converting the string into list & storing into variable.
# ln = len(li) #storing the length of the list into a variable.
# revStr = "" #defining an empty variable (which will be updated & will be final result to check palindrome).
# i = ln - 1 #value of i will be used in loop.
#
# while i >= 0: #here logic is to start from right to left from the list named "li". That means going from last to first index of the list till the index value is "0" of the "li" list.
#     revStr = revStr + li[i] #concatenating & updating the "revStr" defined variable.
#     i = i - 1 #decreasing the value of i to reach from the last index to first index.
# word = word.lower() #converting value into lowercase string.
# revStr = revStr.lower() #converting the final output into lowercase string to avoid case sensitive issue.
#
# if word == revStr: #the two string is same or not?
#     print('Palindrome') #if same.
# else:
#     print('Not palindrome') #if not same.

# word = input()
# li = list(word)
# ln = len(li)
# revStr = ""
# i = ln - 1
#
# while i >= 0:
#     revStr = revStr + li[i]
#     i = i - 1
# word = word.lower()
# revStr = revStr.lower()
#
# if word == revStr:
#     print('Palindrome')
# else:
#     print('Not palindrome')


# import random                      # 1
#                                    # 2
# n_guesses = 0                      # 3
# while n_guesses < 5:               # 4
#     number = random.randint(1, 5)  # 5
#     guess = int(input())           # 6
#     if guess == number:            # 7
#         print('Yes!')              # 8
#     else:                          # 9
#         print('No!')               # 10
#     n_guesses += 1                 # 11


# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

# pancakes = 2
# while pancakes > 0:
#     print("I'm the happiest human being in the world!")
#     pancakes -= 1
#     if pancakes == 0:
#         print("Now I have no pancakes!")
#         # break
# else:
#     print("No pancakes...")

# string = "red yellow fox bite orange goose beeeeeeeeeeep"
# vowels = 'aeiouy'
# count = 0
#
# # fix this for loop
# for i, v in enumerate(string):
#     if string[i] in vowels:
#         count += 1
# print(count)

# a = int(input())
# b = int(input())
# total = 0
# soma = 0
# for i in range(a, b+1):
#     if i % 3 == 0:
#         soma += i
#         total += 1
# print(soma/total)


# numero = int(input())
#
# for i in range(100):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# for i in range (1,12,3):
#     print(i)

# for i in range(0,5):
#     print(i)

# i = 1
# while i <= 20:
#     print(i * i)
#     i += 1
# n = int(input())
# f = 1
# while f <= n:
#     print(f*f)
#     f +=1

# hours = int(input())
# if hours <= 2:
#     print('That seems reasonable')
# elif hours <= 4:
#     print('Do you have time for anything else?')
# else:
#     print('You need to get outside more!')


#
# # problem of day 23/02/20 Ticket
# # Save the input in this variable
# ticket = input()
# # Add up the digits for each half
# half1 = 0
# half2 = 0
# cont = 0
# for i in ticket:
#     if cont <= 2:
#         half1 += int(i)
#     else:
#         half2 += int(i)
#     cont += 1
#
# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")


# from math import floor
# # 200 ml of water, 50 ml of milk, and 15 g
# water = int(input('Write how many ml of water the coffee machine has: '))
# milk = int(input('Write how many ml of milk the coffee machine has: '))
# coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
# amount_of_coffee = int(input('Write how many cups of coffee you will need: '))
# water_necessary = floor(water / 200)
# milk_necessary = floor(milk / 50)
# coffee_beans_necessary = floor(coffee_beans / 15)
# smallest_item = min(water_necessary, milk_necessary, coffee_beans_necessary)
# if amount_of_coffee == smallest_item:
#     print('Yes, I can make that amount of coffee')
# elif amount_of_coffee < smallest_item:
#     sobra = smallest_item - amount_of_coffee
#     print(f"Yes, I can make that amount of coffee (and even {sobra} more than that)")
# elif amount_of_coffee > smallest_item:
#     sobra = -(smallest_item - amount_of_coffee)
#     print(f"No, I can make only {-(sobra - amount_of_coffee)} cups of coffee")
# money = int(input())
# chicken = 23
# goat = 678
# pig = 1296
# cow = 3848
# sheep = 6769
# if chicken <= money < goat:
#     print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
# elif goat <= money < pig:
#     print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
#     # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
# elif pig <= money < cow:
#     print(f'{round(money / pig - 0.5)} pigs' if round(money / pig - 0.5) > 1 else '1 pig')
#     # print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
#     # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
# elif cow <= money < sheep:
#     print(f'{round(money / cow - 0.5)} cows' if round(money / cow - 0.5) > 1 else '1 cow')
#     # print(f'{round(money / pig - 0.5)} pigs' if round(money / pig - 0.5) > 1 else '1 pig')
#     # print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
#     # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
# elif money >= sheep:
#     print(f'{round(money / sheep - 0.5)} sheep' if round(money / cow - 0.5) > 1 else '1 sheep')
#     # print(f'{round(money / cow - 0.5)} cows' if round(money / cow - 0.5) > 1 else '1 cow')
#     # print(f'{round(money / pig - 0.5)} pigs' if round(money / pig - 0.5) > 1 else '1 pig')
#     # print(f'{round(money / goat - 0.5)} goats' if round(money / goat - 0.5) > 1 else '1 goat')
#     # print(f'{round(money / chicken - 0.5)} chickens' if round(money / chicken - 0.5) > 1 else '1 chicken')
#
# else:
#     print('None')


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
