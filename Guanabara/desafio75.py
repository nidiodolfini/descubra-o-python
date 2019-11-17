numeros = (int(input("Digite o primeiro numero: ")), int(input('Digite o segundo numero: ')), int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))
par = 0
for numero in numeros:
    if numero % 2 == 0:
        par += 1

#posicao = 0

print('A: ', numeros.count(9))
# for cont in numeros:
#     if cont == 3:
#         posicao = numeros.index(3)

#print('B: ', posicao)
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu nenhuma vez ')
print('C: ', par)


