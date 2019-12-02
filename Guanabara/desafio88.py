
from random import randint
from time import sleep

lista = list()
jogos = list()

quantidade = int(input('Quantos jogos você quer? '))
totalJogadas = 1
while totalJogadas <= quantidade:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogadas += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)