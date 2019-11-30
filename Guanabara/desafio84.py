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

listaPesados = list()
for pos, valor in enumerate(lista):
    if (pos == 0 or listaPesados[pos] <= lista[pos]):
        print('entrou no IF')


print(len(dados))