class ImprimirTexto:
    def __init__(self, texto):
        self.texto = texto
        self.seila = 'eu iniciei'
        print(self.seila, self.texto)


lista = {'testea': 'teste1', 'teste': 'teste2'}

teste = ImprimirTexto(lista)


listaTeste = list(range(0, 10))

print(listaTeste)

tupla = tuple(range(0, 10))

print(tupla)

tupla2 = ('Nidio', 33)

print(tupla2)

nome, idade = tupla2

print(nome)