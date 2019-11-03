conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print("União: {} ".format(conjunto_uniao))

conjunto_intersecao = conjunto.intersection(conjunto2)
print("intersecção: {}".format(conjunto_intersecao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
print("diferença do 1 e 2 {}".format(conjunto_diferenca1))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print("diferença do 2 e 1 {}".format(conjunto_diferenca2))

lista = ["cachorro", "cachorro", "gato", "gato", "rato", "porquinho da india"]

conjunto_animais = set(lista) #conjunto retira a duplicidade da lista
print(lista)

print(conjunto_animais)