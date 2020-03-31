name = "John"


def change_name(new_name):
    global name
    name = new_name


change_name("Mary")
print(name)



# text = input()
# counter = 0
# error = False
# for i in text:
#     if text[0] == ')':
#         error = True
#     elif i == '(':
#         counter += 1
#     elif i == ')':
#         counter -= 1
# if error:
#     print('ERROR')
# elif counter == 0:
#     print('OK')
# else:
#     print('ERROR')

# books = []
# count = int(input())
# read = []
#
# for _ in range(count):
#     action = input().split(' ',1)
#     if action[0] == 'BUY':
#
#         books.append(action[1])
#     elif action[0] == 'READ':
#         read.append(books[-1])
#
# for i in read:
#     print(i)

# from math import sqrt
#
# number = int(input())
# zero = number
# numbers = []
# numbers.append(number)
# while zero != 0:
#     number = int(input())
#     if number == 0 and len(numbers) == 0:
#         print(0)
#         break
#     numbers.append(number)
#     zero += number
# soma = 0
#
# for i in numbers:
#     # print(i)
#     soma += i**2
# print(soma)
# print(zero)
# n = int(input())
# my_stack = []
# for i in range(n):
#     my_stack.append(input())
#
# for i in range(len(my_stack), 0,-1):
#     print(my_stack[i-1])

# kind_food = input()
# if kind_food == 'pizza':
#     print('Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy')
# elif kind_food == 'salad':
#     print('Caesar salad, Green salad, Tuna salad, Fruit salad')
# elif kind_food == 'soup':
#     print('Chicken soup, Ramen, Tomato soup, Mushroom cream soup')
# else:
#     print("Sorry, we don't have it in the menu")


# class RightTriangle:
#     def __init__(self, hyp, leg_1, leg_2):
#         self.c = hyp
#         self.a = leg_1
#         self.b = leg_2
#         self.area = self.a * self.b * 0.5
#         if (self.c**2) == ((self.a**2) + (self.b**2)):
#             print(self.area)
#         else:
#             print('Not right')

# print(5**2, 3**2, 4**2)
# area = ((3) * (4))* 0.5
# print(area)
# c, a, b = input().split(' ')
# RightTriangle(int(c), int(a), int(b))

# email = 'nidiosdolfini@gmail.com'
# # slice_email = email.split('@')
# # print(slice_email[0])
# index = email.index('@')
# print(index)
# print(email[:index])

# class Mountain:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     # create convert_height here
#     def convert_height(self):
#         self.foot = self.height / 0.3048
#         return (f'{self.foot}')
#
#
# # create mountains here
# everest = Mountain('Everest', 8848)
# aconcagua = Mountain('Aconcagua', 6960.8)
# print(everest.convert_height(), aconcagua.convert_height())


# import os
#
#
# def arraySum(numbers):
#     print(sum(numbers))
#
#
#
# numbers = [1,2,3,4,5]
# arraySum(numbers)

# def lastLetters(word):
#     # Write your code here
#     last = ''
#     for i in range(len(word)-1, len(word)-3, -1):
#         last += ''.join(word[i])+ ' '
#     return last
#
# print(lastLetters('APPLE'))
# def fizzBuzz(n):
#     # Write your code here
#     i = 1
#     while i <= n:
#         if i % 3 == 0:
#             print("Fizz", end="")
#             if i % 5 == 0:
#                 print("Buzz", end="")
#         elif i % 5 == 0:
#             print("Buzz", end="")
#         else:
#             print(i, end="")
#         print()
#         i += 1
#
# fizzBuzz(15)
# word = input()
#
# for i, v in enumerate(word):
#     print(v if i % 2 != 0 else "", end='')
#

# deposit = int(input())
# years = 0
# while deposit <= 700000:
#     years +=1
#     tax = (deposit * 7.1) / 100
#     deposit += tax
# print(years)

# words = input().split(' ')
# word_with_s =[] #str(words).endswith('s')
# for word in words:
#     if word.endswith('s'):
#        word_with_s.append(word)
# for i in range(len(word_with_s)):
#     if i < len(word_with_s)-1:
#         print(word_with_s[i], end='_')
#     else:
#         print(word_with_s[i], end='')
#
# print("_".join(w for w in input().split() if w.endswith('s')))
# n = int(input())
# k = int(input())
# print(round(k % n))
#

# f1 = open('one.txt', 'w')
# f2 = open('two.txt', 'w')
# f3 = open('three.txt', 'w')
#
# print('start', 'end', sep=' & ', file=f1)  # [1]
# print('start', file=f2, flush=True)
# f3.write('end')  # [2]
# print('end', file=f2, flush=True)  # [3]
#
# f1.close()  # [4]
# f2.close()  # [5]
# f3.close()  # [6]


# import sys
#
#
# def division():
#     a = int(input("Set the first number: "))
#     b = int(input("Set the second number: "))
#     if b != 0:
#         print(a / b)
#     else:
#         # The string below will look like an error message.
#         print("The second number cannot be a zero!", file=sys.stderr)
#
# division()
# print('teste')

# print('The specified string to be written', file='text_file.txt')

# import sys
#
#
# def division():
#     a = int(input("Set the first number: "))
#     b = int(input("Set the second number: "))
#     if b != 0:
#         print(a / b)
#     else:
#         # The string below will look like an error message.
#         print("The second number cannot be a zero!", file=sys.stderr)
#
# division()
# my_file = open('testfile.txt', 'w')
# print('This string will be in the file...', file=my_file)
# my_file.close()


# animals = open('animals.txt', encoding='utf-8')
# animals_new = open('animals_new', 'w', encoding='utf-8')
# for i in animals:
#     animals_new.writelines(i.replace('\n', ' '))

# entrada = input()
# arq = open('animals.txt', 'w', encoding='utf-8')
# arq.write(entrada)
# arq.close()

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# solar_system = open('solar_system.txt', 'w', encoding='utf-8')
# for planet in planets:
#     solar_system.write(planet + '\n')
#
# solar_system.close()
# color_list = ['cyan', 'magenta', 'yellow', 'key color']
#
# cymk_file = open('CMYK.txt', 'w', encoding='utf-8')
# cymk_file.writelines(color_list)
# cymk_file.close()

# names = ['Kate', 'Alexander', 'Oscar', 'Mary']
#
# name_file = open('names.txt', 'w+', encoding='utf-8')
#
# # write the names on separate lines
# name_file.writelines(names)
# print(name_file.read())
# name_file.close()


# seasons_file = open('teste.txt', encoding='utf-8')
#
# for i in seasons_file:
#     a, b = i.split(' ')
#     print(int(a) + int(b))
# seasons_file.close()
# dct = {}
# list = []
# for i in teste:
#     dct['name'],dct['points'] = i.split(' ')
#     list.append(dct)
#     dct.clear()
# print(dct)
# print(list)
# print(list[1]['name'])
# def fun(x):
#     if x % 2 ==0:
#         return 1
#     else:
#         return 2
# print(fun(fun(2)))
# print("I am = I'm")
# print("I have = I've")
# print("I will = I'll")
# print("I had / would = I'd")

# def f(x):
#     if x <= -2:
#         resultado = 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         resultado = - x / 2
#     else:
#         resultado = (x - 2) ** 2 + 1
#     print(resultado)
#
#
# # f(-4.5)
# f(4.5)
# f(1)

# print('''"""
# THIS IS A STRING
# """
# ''')


# import sys
#
# args = sys.argv
#
# # the variable "args" is already defined
# my_list = []  # your code here
#
# my_list = [int(args[1]), int(args[2]), int(args[3]), int(args[4])]
#
# print(str(my_list))
# # print(input().strip("*_~`"))
#

# string = input()
# print(list(string))

# class Stack():
#     fila = []
#
#     def __init__(self):
#         pass
#
#     def push(self, el):
#         self.fila.append(el)
#
#     def pop(self):
#         ultimo = self.fila[-1]
#         self.fila.remove(self.fila[-1])
#         return ultimo
#
#     def peek(self):
#         return self.fila[-1]
#
#     def is_empty(self):
#         if len(self.fila) == 0:
#             return True
#         else:
#             return False

#
# filas = Stack()
# print(filas.is_empty())
# filas.push('Teste')
# print(filas.fila)
# filas.push('Testes')
# print(filas.fila)
# print(filas.pop())
# print(filas.fila)
# print(filas.is_empty())
# print(filas.peek())
#
# # #  Posted from EduTools plugin
# # class Stack():
# #
# #     def __init__(self):
# #         self.elements = []
# #
# #     def push(self, el):
# #         self.elements.append(el)
# #
# #     def pop(self):
# #         return self.elements.pop()
# #
# #     def peek(self):
# #         return self.elements[-1]
# #
# #     def is_empty(self):
# #         if self.elements:
# #             return False
# #         else:
# #             return True
