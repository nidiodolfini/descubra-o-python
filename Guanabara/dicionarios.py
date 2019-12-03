# tuplas ()
# listas []
# dicionarios = {}
# dicionarios = dict{}
#
# pessoas = { 'nome': 'Nidio', 'sexo': 'M', 'idade': 33}
# print(pessoas)
#
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
#
# del pessoas['sexo']
# pessoas['nome'] = 'Sophia'
# pessoas['peso'] = 115.50
# for k in pessoas.keys():
#     print(f'chave {k}')
#
# for v in pessoas.values():
#     print(f'valores {v}')
#
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(estado1)
# print(brasil[1]['uf'])
#
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla:'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())

# for e in brasil:
#     for v in e.values():
#         print(v)


# for p, e in enumerate(brasil):
#    print(brasil[p]['sigla'])