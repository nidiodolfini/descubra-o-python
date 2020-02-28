set1 = {'oatmeal', 'millet', 'rice', 'semolina', 'buckwheat'}
set2 = {'oatmeal', 'rice', 'semolina', 'milet', 'buckwheat'}
print(set1 == set2)

# word = input()  # the input word
#
# print(len(set(word)))
# teste = set(word)
# teste.remove('s')
# print(teste)
# import random
#
# word = random.choice(['python', 'java', 'kotlin', 'javascript'])
# hidden_word = '-' * (len(word))
#
# print(word , ' ', hidden_word)
# for i in range(8):
#     if input() in word:
#         print('tem')
# import random
#
# r = random.choice(["Voldemort", 'harry', 'numlembro'])
# print(r)
# import math
# x = int(input())
# print(math.expm1(x))
# # import math
# # x = int(input())
#
# # use factorial() here
# print(math.factorial(x))

# dragons = ['Rudror', 'Targiss', 'Coporth']
# dragons.sort(reverse=True)
# print(dragons)
# dragons.insert(2, -10)
# print(dragons)
# dragons.reverse()
# print(dragons)
#


# # work with this variable
# shopping_list = []
#
# shopping_list.append("milk")
# shopping_list.append("olive oil")
# shopping_list.append("bananas")
# shopping_list.list.remove("milk")
# shopping_list.append("brownie")
# put the rest of list operations below

# my_list = ['Mary', 'Bob', 'Pete', 'Jane']
# my_list.append(my_list.sort())
# print(my_list)

# numbers = [2, 2, 4, 1, 1, 3, 5]
# numbers.sort(reverse=True)
# numbers.remove(2)
# numbers.remove(1)
# numbers.remove(5)
# numbers.append(5)
#
# print(numbers)

# dragons = []
#
# dragons = 'teste'
# # dragons = 'verde'
# dragons.append('Targiss')
# print(dragons)
# print(type(dragons))


# def create_url(host='localhost', port=443):
#     return f'https://{host}:{port}'
#
# print(create_url('nidio', 8080))

# def square_odds(a, b):
#     start = a
#     if a % 2 == 0:
#         start += 1
#     end = b + 1
#     for odd in range(start, end, 2):
#         print(odd ** 2)
#
#
# # from 22 to 42
# square_odds(22, 42)
#
# # from 15 to 31
# square_odds(b=15, a=31)
#
# # from 42 to 49
# square_odds(49, 42)

# first_name = input()
# last_name = input()
#
# # create full_name here
# b = (first_name, last_name)
# print(b)
# print(type(b))
#

# a = ()
# b = tuple()
# c = ([])
# # d = (,)
# e = tuple('')
# print(type(a))
# print(type(b))
# print(type(c))
# # print(type(d))
# print(type(e))

# a = [1, 2, 3]
# b = a
# # what is the value of b?
# print(b)
# a[1] = 10
# # and here?
# print(b)
# b[0] = 20
# # what about now?
# print(b)
# a = [5, 6]
# # it is the last time, we promise. The value of b?
#
# print(a)


# class MyClass:
#     n_objects = 0
#
#     def __new__(cls):
#         if cls.n_objects < 5:
#             instance = object.__new__(cls)
#             cls.n_objects += 1
#             return instance
#
#     def __str__(self):
#         return "An object of MyClass"
#
# classe = MyClass()
# print(classe)
# class Puppy:
#     n_puppies = 0
#
#     # define __new__
#     def __new__(cls):
#         if cls.n_puppies < 10:
#             instance = object.__new__(cls)
#             cls.n_puppies += 1
#             return instance
# pup1 = Puppy()
# pup2 = Puppy()
# pup3 = Puppy()
# pup4 = Puppy()
# pup5 = Puppy()
# pup6 = Puppy()
# pup7 = Puppy()
# pup8 = Puppy()
# pup9 = Puppy()
# pup10 = Puppy()
# pup11 = Puppy()
# pup12 = Puppy()
# print(pup11)


# class Patient:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name =last_name
#         self.age = age
#
#     # create methods here
#     def __repr__(self):
#         return f'Object of the class Patient. name: {self.name}, last_name: {self.last_name}, age: {self.age}'
#
#     def __str__(self):
#         return f'{self.name} {self.last_name}. {self.age}'
#
# john = Patient("John", "Doe", 50)
#
# print(john)
# class Lightbulb:
#     def __init__(self):
#         self.state = "off"
#
#     # create method change_state here
#     def change_state(self):
#         if self.state == 'off':
#             self.state = 'on'
#             print('Turning the light on')
#         else:
#             self.state = 'off'
#             print('Turning the light off')
#
# luz = Lightbulb()
# print(luz.state)
# print(luz.change_state())
# print(luz.state)
# print(luz.change_state())
# class PiggyBank:
#     # create __init__ and add_money
#     def __init__(self, dollars, cents):
#         self.dollar = dollars
#         self.cents = cents
#
#     def add_money(self, deposit_dollars, deposit_cents):
#         self.dollar += deposit_dollars
#         if self.cents + deposit_cents > 99:
#             self.dollar += (self.cents + deposit_cents) // 100
#             soma = (self.cents + deposit_cents) % 100
#             self.cents = soma
#         else:
#             self.cents += deposit_cents
#         return self.dollar
#         return self.cents
#
#
# porco = PiggyBank(0, 155)
# porco.add_money(0, 50)

# class House:
#     def __init__(self, floors):
#         self.floors = floors
#         self.color = ''
#
#     # create the method here
#     def paint(self, color):
#         self.color = color

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f"Hello, I am {self.name}!")
#
#
# david = Person(input())
# david.greet()
# create the method greet here
# # our class Ship
# class Ship:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#
#     # the old sail method that you need to rewrite
#     def sail(self, country):
#         print(f'The {self.name} has sailed for {country}!')
#
#
# black_pearl = Ship("Black Pearl", 800)
# black_pearl.sail('Argentina')


# class Mountain:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     # create convert_height here
#     def convert_height(self):
#         self.foot = self.height * 0.3048
#         return self.foot
#
#
# # create mountains here
# everest = Mountain('Everest', 8848)
# aconcagua = Mountain('Aconcagua', 6960.8)
# print(Mountain.convert_height(everest))
# print(aconcagua.convert_height())

# class Door:
#     def open_door(self):
#         print("Door open")
#
#
# door = Door()
# Door.open_door()


# def fahrenheit_to_celcius(fah):
#     print((float(fah) - 32) * 5 / 9)
#
# fahrenheit_to_celcius(input())

# class Sphere:
#     pi = 3.14
#
#     def __init__(self, r):
#         self.r = r
#         self.v = (4 * self.pi * (r**3)) / 3
#         print(f'{self.v:.2f}')
#
#
# bola = Sphere(int(input()))
# class Painting:
#     n_painting = 0
#     museum_name = ''
#
#     def __init__(self, title, artist, year):
#         self.title = title
#         self.artist = artist
#         self.year = year
#         print(f'"{title}" by {artist} ({year}) hangs in the Louvre.')
#
#
# paint = Painting(input(), input(), input())
#
#

# class Fish:
#     place = "aquarium"
#     n_fish = 0  # number of fish in the aquarium
#
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#
#
# greg = Fish("Greg", "guppy")
# # Fish.n_fish = 1
# greg.n_fish = 1
# print(Fish.n_fish)

# class City:
#     all_cities = []
#
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#
# ny = City("New York", 1624)
# ny.all_cities.append("New York")
#
# stockholm = City("Stockholm", 1187)
# stockholm.all_cities = ["Stockholm"]
#
# print(stockholm.all_cities)
# # class Student:
#
#     def __init__(self, name, last_name, birth_year):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         self.id = self.name[0] + self.last_name + str(self.birth_year)
#         print(self.id)
#
#
# # name = input()
# # last_name = input()
# # birth_year = int(input())
# # student = Student(name, last_name, birth_year)
# student = Student(input(), input(), input())
# print(student.id)

# class Movie:
#     def __init__(self, title, director, year):
#         self.title = title
#         self.director = director
#         self.year = year
#
#
# # objects of the class Movie
# titanic = Movie('Titanic', 'James Cameron', 1997)
# star_wars = Movie('Star Wars', 'George Lucas', 1977)
# fight_club = Movie('Fight Club', 'David Fincher', 1999)
#
# print(titanic.year)

# class Angel:
#     color = "white"
#     feature = "wings"
#     home = "Heaven"
#
#
# class Demon:
#     color = "red"
#     feature = "horns"
#     home = "Hell"
#
# procura = ''
# find = input().split(' ')
# for v in find:
#     if v in ['white', 'wings', 'Heaven', 'red', 'horns', 'Hell']:
#         # print(v)
#         procura = v
#     else:
#         procura = 'No match'
# # print(procura)
# if procura in getattr(Angel, 'home') or procura in getattr(Angel, 'feature') or procura in getattr(Angel, 'color'):
#     print('Angel')
# elif procura in getattr(Demon, 'home') or procura in getattr(Demon, 'color') or procura in getattr(Demon, 'feature'):
#     print('Demon')
# else:
#     print('No match')
# class RockBand:
#     genre = 'Rock'
#     n_members = 4
#     famous_songs = []
#
#
# kiss = RockBand()
# print(kiss.genre)
# print(kiss.n_members)
# print(kiss.famous_songs)

# # Book class
# class Book:
#     material = "paper"
#     cover = "paperback"
#     all_books = []
#
# my_book = Book()
#
# print(my_book.cover)


# income = int(input())
# percent = 1
# calculated_tax = 0
# if income <= 15527:
#     percent = 0
#     calculated_tax = 0
# elif income <= 42707:
#     percent = 15
#     calculated_tax = (income * 15) / 100
# elif income <= 85414:
#     percent = 22
#     calculated_tax = (income * 22) / 100
# elif income <= 132406:
#     percent = 26
#     calculated_tax = (income * 26) / 100
# else:
#     percent = 28
#     calculated_tax = (income * 28) / 100
#
# print(f"The tax for {income} is {percent}%. That is {calculated_tax:.2f} dollars!")

# string1 = "someone"
# string2 = "string"
# # add the correct string instead of the dots
# print(string1 + "'s " + string2)
#
# # # i = 1
# n = (f''''
# '"'
# '"'"'
# '"'"'"'
# ''')
# print(n)

# n = 829
# soma = 0
# t = list(str(n))
# for i in t:
#     soma += int(i)
# print(soma)
# # x = float(input())
# y = float(input())
# if x < 0 and y < 0:
#     print('III')
# elif y < 0 and x > 0:
#     print('IV')
# elif x < 0 and y > 0:
#     print('II')
# elif x > 0 and y > 0:
#     print('I')
# else:
#     print('(0, 0)')
#


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
