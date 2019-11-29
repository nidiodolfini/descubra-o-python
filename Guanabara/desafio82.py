num = []
par = list() # tudo listas
impar = []
while True:
    num.append(int(input('digite um numero: ')))
    resp = str(input( 'quer continuar'))
    if resp in 'Nn':
        break

for posicao, valor in enumerate(num):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)


print(F'LISTA COMPLETA {num}')
print(f'lista de pares {par}')
print(f'lista de impares {impar}')