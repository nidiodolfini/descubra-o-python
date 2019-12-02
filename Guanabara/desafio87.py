lista = [[0,0,0], [0,0,0],[0,0,0]]
par = 0
soma = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um valor na posição: [{l},{c}] '))

for l in range(0,3):
    for c in range(0,3):
       if lista[l][c] % 2 == 0:
           par += lista[l][c]

for c in range(0,3):
   soma += lista[c][2]


for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()

print('-='*30)
print(soma)
print(par)
print(max(lista[1]))