numero = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
    else:
        print('Valor duplicado')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numero.sort()
print(f'Você adicionou os valores {numero}')