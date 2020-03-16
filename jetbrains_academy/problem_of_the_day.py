words = input().split(' ')
word_with_s =[] #str(words).endswith('s')
for word in words:
    if word.endswith('s'):
       word_with_s.append(word)
for i in range(len(word_with_s)):
    if i < len(word_with_s)-1:
        print(word_with_s[i], end='_')
    else:
        print(word_with_s[i], end='')

print("_".join(w for w in input().split() if w.endswith('s')))
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
