dados = input().split(" ")

a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

pi = 3.14159

triangulo = (a * c) / 2
circulo = (c ** 2) * pi
trapezio = (( a + b) * c) /2
quadrado = b * b
retangulo = a * b

print("TRIANGULO: %0.3f" %triangulo)
print("CIRCULO: %0.3f" %circulo)
print("TRAPEZIO: %0.3f" %trapezio)
print("QUADRADO: %0.3f" %quadrado)
print("RETANGULO: %0.3f" %retangulo)