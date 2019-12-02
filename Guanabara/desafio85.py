lista = [[],[]]
numero = 0
for i in range(1,8):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)



lista[0].sort()
lista[1].sort()

print(lista[0])
print(lista[1])