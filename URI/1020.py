dias = int(input())
ano = 0
mes = 0
dia = 0

while dias > 0:
    if dias >= 365:
        ano = ano + 1
        dias = dias - 365
    elif dias >= 30:
        mes = mes + 1
        dias = dias -30
    else:
        dia = dias
        dias = 0

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))