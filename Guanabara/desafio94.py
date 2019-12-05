

pessoas = list()
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo M/F: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    print(pessoa)
    pessoas.append(pessoa.copy())
    resp = (input('Deseja continuar: '))
    if resp in "nN":
        break


print(len(pessoas))
soma = 0
for i, v in enumerate(pessoas):
    soma += pessoas[i]["idade"]
    if pessoas[i]["sexo"] in "Ff":
        print(pessoas[1]["nome"])
    if pessoas[i]['idade'] > soma/len(pessoas):
        print(pessoas[i]['nome'])


print(soma/len(pessoas))