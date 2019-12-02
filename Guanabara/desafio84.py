temp = []
dados = []
maior = menor = 0
while True:
    temp.append(str(input('digite o nome: ')))
    temp.append(int(input('Digite o peso: ')))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]    
        if temp[1] < menor:
            menor = temp[1]

    dados.append(temp[:])
    temp.clear()


    print('menor peso' , menor, ' maior peso' , maior)
    resp = str(input('quer continuar: '))
    if resp in 'Nn':
        break
print('os mais pesados são: ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print('os menores pesos foram: ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
print(f' numeros de pessoas na lista {len(dados)}')