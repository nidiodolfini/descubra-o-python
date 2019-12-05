

pessoas = list()
pessoa = dict()
soma = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo M/F: ')).upper()[0]
    pessoa['idade'] = int(input('Digite a idade: '))
    print(pessoa)
    soma += pessoa["idade"]
    pessoas.append(pessoa.copy())
    resp = (input('Deseja continuar: '))
    if resp in "nN":
        break


print(len(pessoas))

for i, v in enumerate(pessoas):
    if pessoas[i]['idade'] > soma/len(pessoas):
        print(pessoas[i]['nome'])

for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'])

print(soma/len(pessoas))