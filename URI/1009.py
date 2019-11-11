nome = input()
salario = float(input())
vendas = float(input())

bonus = (vendas / 100) * 15

print("TOTAL = R$ %0.2f" %(salario + bonus))
