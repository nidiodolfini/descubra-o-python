# a,w,e = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis

# # Converte o valor para os tipos necessários 
# a = int(a)
# w = int(w)
# e = float(e) 

lista = input().split(" ") 
lista2 = input().split(" ") 
codigo_peca = int(lista[0])
numero_de_peca = int(lista[1])
valor_pecas = float(lista[2])
codigo_peca2 = int(lista2[0])
numero_de_peca2 = int(lista2[1])
valor_pecas2 = float(lista2[2])

valor_total = (numero_de_peca * valor_pecas) + (numero_de_peca2 * valor_pecas2)

print("VALOR A PAGAR: R$ %0.2f" %valor_total)