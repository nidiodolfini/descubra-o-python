lista = []
dados = []
while True:
    lista.append(str(input('digite o nome: ')))
    lista.append(int(input('Digite o peso')))
    dados.append(lista[:])
    lista.clear()

    resp = str(input( 'quer continuar'))
    if resp in 'Nn':
        break

print(len(dados))