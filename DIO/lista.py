lista = [1, 2, 5, 9, 7]
lista_animal = ["porquinho da india", "gato", "cachorro", "passaro"]

tupla = (1, 3, 2 , 5 , 6 , 4 , 7, 9, 10) # tulha é igual lista só que é colocado () e não aceita ser a alteração de valores

print(len(tupla))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal)) # converte lista em tuple
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))


# lista.sort() # ordena a lista
# lista_animal.sort()
# print(lista)
# print(lista_animal)

# lista.reverse()
# print(lista)

# print(lista[2])
# print(sum(lista))
# print(max(lista))
# print(max(lista_animal))
# nova_lista = lista * 3
# print(nova_lista)

# for x in lista_animal:
#     print(x)


# if "lobo" in lista_animal:
#     print("existe um gato na lista")
# else:
#     print("não existe um gato na lista")
#     lista_animal.append("lobo")

# print(lista_animal)

# lista_animal.pop(2) #retira o ultimo da lista se não tiver nenhum indice ou retira do indice marcado
# lista_animal.remove("gato") #remnove vai excluir o item que você colocou
# print(lista_animal)