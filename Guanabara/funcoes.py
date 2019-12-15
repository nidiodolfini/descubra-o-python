# def mostrarlinha(texto):
#     print('-=' * 30)
#     print(texto)
#     print('=-' * 30)
#
#
# mostrarlinha("nidio")
#
#
# def soma(a=0, b=0):
#     print(f'A = {a} e B = {b}')
#     print(a + b)
#
#
# soma(b=5, a=6)
# soma(7, 3)
# soma()
#
#
# def contador(*num):
#     """
#     -faz a soma de N numeros
#
#     """
#
#     print(sum(num))
#
#
# help(contador)
#
# contador(1, 2, 3)
# contador(1, 2, 3, 4, 5, 6, 7)
#
#
# def listaa(lst):
#     print(lst)
#
#
# lsita = [0, 1, 2, 3, 4]
#
# listaa(lsita)
#
# help(input())
#

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a vale {a}')
    print(f'B vale {b}')


a = 5
teste(a)
