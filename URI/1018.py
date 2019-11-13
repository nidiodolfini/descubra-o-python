valor = int(input())
valor_inteiro = valor
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

while valor > 0:
    if valor >= 100:
        cem = cem + 1
        valor = valor - 100
    elif valor >= 50:
        cinquenta = cinquenta + 1
        valor = valor - 50
    elif valor >= 20:
        vinte = vinte + 1
        valor = valor -20
    elif valor >= 10:
        dez = dez + 1
        valor = valor - 10
    elif valor >= 5:
        cinco = cinco + 1
        valor = valor - 5
    elif valor >= 2:
        dois = dois + 1
        valor = valor -2
    else:
        um = valor
        valor = 0
        
print(valor_inteiro)
print(cem, "nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(um, "nota(s) de R$ 1,00")