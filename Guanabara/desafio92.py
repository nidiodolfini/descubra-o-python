dados = dict()
dados['nome'] = str(input('Nome: '))
dados['Idade'] = 2019 - int(input('Ano de Nascimento: '))
dados['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['cpts'] > 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = 32 - (2019 - (dados['contratacao'] + dados['Idade']))

for k, v in dados.items():
    print(f'{k} tem o valor {v}')

print(dados)