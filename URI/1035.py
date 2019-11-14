numeros = input().split(" ")

a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
d = int(numeros[3])

if ((a % 2 == 0) and (b > c) and (d > a) and ( c + d > a + b)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")