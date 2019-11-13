valor = float(input())
valor_inteiro = valor
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
cinquenta_centavos = 0
vintecinco_centavos = 0
dez_centavos = 0
cinco_centavos = 0
um_centavo = 0


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
    elif valor >= 1:
        um = um + 1
        valor = valor - 1
    elif valor >= 0.50:
        cinquenta_centavos = cinquenta_centavos + 1
        valor = valor - 0.50
    elif valor >= 0.25:
        vintecinco_centavos = vintecinco_centavos + 1
        valor = valor - 0.25
    elif valor >= 0.10:
        dez_centavos = dez_centavos + 1
        valor = valor - 0.10
    elif valor >= 0.05:
        cinco_centavos = cinco_centavos + 1
        valor = valor - 0.05
    elif ((valor // 0.01) >= 0.01):
        um_centavo = um_centavo + 1
        valor = valor - 0.01
    else:
        valor = 0
        
print("NOTAS:")
print(cem, "nota(s) de R$ 100.00")
print(cinquenta, "nota(s) de R$ 50.00")
print(vinte, "nota(s) de R$ 20.00")
print(dez, "nota(s) de R$ 10.00")
print(cinco, "nota(s) de R$ 5.00")
print(dois, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(um, "moeda(s) de R$ 1.00")
print(cinquenta_centavos, "moeda(s) de R$ 0.50")
print(vintecinco_centavos, "moeda(s) de R$ 0.25")
print(dez_centavos,"moeda(s) de R$ 0.10")
print(cinco_centavos,"moeda(s) de R$ 0.05")
print(um_centavo, "moeda(s) de R$ 0.01")
