def mostrarlinha(texto):
    print('-=' * 30)
    print(texto)
    print('=-' * 30)


mostrarlinha("nidio")


def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(a + b)


soma(b=5, a=6)


def contador(*num):
    print(sum(num))


contador(1, 2, 3)
contador(1, 2, 3, 4, 5, 6, 7)


def listaa(lst):
    print(lst)


lsita = [0, 1, 2, 3, 4]

listaa(lsita)

help(input())
