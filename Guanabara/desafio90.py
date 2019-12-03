aluno = dict()
# nome = str(input("Digite o nome do aluno"))
# media = float(input("Digite a média do aluno"))
aluno['Nome'] = str(input("Digite o nome do aluno:"))
aluno['media'] = float(input("Digite a média do aluno: "))

if aluno['media'] >= 7:
    print('Aprovado')
else:
    print('reprovado')


print(aluno)