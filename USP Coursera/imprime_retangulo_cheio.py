largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = 1
y = 1
while x <= altura:
    
    while y <= largura:
        print("#", end="")
        y = y + 1
    print()
    x = x + 1
    y = 1
