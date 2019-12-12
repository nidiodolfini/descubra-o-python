from random import randint

numeros = list()
def somaPar(numeros):
    total = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            total += v
    print(total)

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(1, 10))
    print(numeros)


sorteia()
somaPar(numeros)