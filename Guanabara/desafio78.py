numeros = []
menor = 0
maior = 0
for i in range(5):
    numeros.append(int(input(f"Digite um numero para posição {i}: ")))
    if i == 0:
        menor = maior = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()