lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #tuplas tem (), mas para referenciar um objeto dentro da tupla []
#lanche[1] = 'batata frita' tuplas são imataveis, não pode adicionar um novo valor
print(lanche[-1])
print(lanche[0:2])
print(lanche[:2])
print(lanche[:-2])


for comida in lanche:
    print(f'eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])
    print(cont)


for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')


print(sorted(lanche))
print(lanche)

a = (0, 1, 2, 3, 5,)
b = (4, 6, 7, 8, 9, 2)
c = a + b
d = b + a
print('A', a)
print('B', b)
print('C', c)
print('B', d)

print(c.count(2))
print(c.index(2))
print(c.index(2,3)) # procura onde está o valor no caso 2, depois da virgula ele seta apartir de qual posição começar

print(lanche.count('suco'))