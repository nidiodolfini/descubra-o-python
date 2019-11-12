dados = input().split(" ")

a = int(dados[0])
b = int(dados[1])
c = int(dados[2])

if a > b and a > c:
    print(a ,"eh o maior")
elif b > a and b > c:
    print(b , "eh o maior")
else:
    print(c, "eh o maior")