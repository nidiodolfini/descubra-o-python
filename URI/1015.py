import math
dados = input().split(" ")
dados2 = input().split(" ")

x1 = float(dados[0])
x2 = float(dados2[0])
y1 = float(dados[1])
y2 = float(dados2[1])


distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print("%0.4f"%distancia)
