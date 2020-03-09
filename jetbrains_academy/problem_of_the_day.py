import sys

args = sys.argv

# the variable "args" is already defined
my_list = []  # your code here

my_list = [int(args[1]), int(args[2]), int(args[3]), int(args[4])]

print(str(my_list))
# print(input().strip("*_~`"))
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