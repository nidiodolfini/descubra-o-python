valores = []
while True:
    valores.append(int(input("digite um valor")))
    resp = str(input('quer continuar SN'))
    if resp in 'Nn':
        break


print(f' numero de numeros digitados {len(valores)}')
valores.sort(reverse=True)
print(f'valores na ordem descrescente {valores}')
if 5 in valores:
    print(f'o 5 está na lista')
else:
    print('cinco não está na lista')