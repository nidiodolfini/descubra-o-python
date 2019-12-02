ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? S/N: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('_'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_'*26)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]} ')
print('Volte sempre')



# dadosAlunosTemp = list()
# dadosAlunos = list()
# print('Digita o nome e as notas dos alunos: ')
# while True:
#     dadosAlunosTemp.append(str(input('Digite o nome do aluno: ')))
#     dadosAlunosTemp.append(float(input('Digite a primeira nota: ')))
#     dadosAlunosTemp.append(float(input('Digite a segunda nota: ')))
#
#     dadosAlunos.append(dadosAlunosTemp[:])
#     dadosAlunosTemp.clear()
#     resp = str(input('Quer continuar? '))
#     if resp in 'Nn':
#         break
# print(f'NO. Nome     Média')
# for i, l in enumerate(dadosAlunos):
#     print(f'{i:^3} {l[0]:^8} {(l[1]+l[2])/2}')
#
# interrompe = 0
# while interrompe != 999:
#     interrompe = int(input('mostrar nota de qual aluno: (999 interrompe): '))
#     if interrompe <= len(dadosAlunos):
#         print(f'Notas de {dadosAlunos[interrompe][0]} são [{dadosAlunos[interrompe][1], dadosAlunos[interrompe][2]}]')
# print('saiu')