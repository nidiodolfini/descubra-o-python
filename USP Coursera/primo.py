
numero_digitado = int(input("entre com um numero: "))
for numero in range(numero_digitado + 1):
    div = 0
    for x in range(1, numero + 1):
        resto = numero % x
        if resto == 0:
            div += 1
    if div == 2:
        print(numero)





# numero = int(input("Digite um numero: "))

# div = 0

# for x in range(1, numero + 1):
#     resto = numero % x
#     print(x, resto)
#     if resto == 0:
#         div += 1

# if div == 2:
#     print("numero {} é primo".format(numero))
# else:
#     print("numero {} não é primo".format(numero))