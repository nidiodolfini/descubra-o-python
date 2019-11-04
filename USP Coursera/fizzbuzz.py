numero = float(input("digite um valor: "))
if(numero == int(numero)):
    if(numero % 3 == 0 and numero % 5 == 0):
        print("FizzBuzz")
    else:
        print(numero)