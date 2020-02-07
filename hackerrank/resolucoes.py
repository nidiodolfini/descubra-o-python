n = int(input())
contato = {}
contatos = list()
nome = list()
for c in range(0,n):
    arr = list(input().rstrip().split())
    contato['name'] = arr[0]
    contato['phone'] = arr[1]
    contatos.append(contato.copy())
for c in range(0,n):
    nome += list((input().rstrip().split()))
for i in range(0,n):
    pesquisa = nome[i]
    if pesquisa in contatos[i]['name']:
        print(f'{contatos[i]["name"]}={contatos[i]["phone"]}')
    else:
        print('Not found')
import sys

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')