from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['Idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
dados['cpts'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['cpts'] > 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = dados['Idade'] + ((dados['contratacao'] + 35) -datetime.now().year)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')

print(dados)