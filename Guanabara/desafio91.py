from random import randint
jogada = dict()
jogadas = []
for cont in range(0,4):
    jogada['numero'] = randint(1,6)
    jogadas.append(jogada.copy())
    print(jogadas)

print(jogadas)