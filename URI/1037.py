numero = float(input())

if numero >= 0 and numero <= 25.0000:
    print("Intervalo [0,25]")
elif numero >= 25.0001 and numero <= 50.0000000:
    print("Intervalo (25,50]")
elif numero >= 50.0000001 and numero <= 75.0000000:
    print("Intervalo (50,75]")
elif numero >= 75.0000001 and numero <= 100.0000000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
