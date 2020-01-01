class ImprimirTexto:
    def __init__(self, texto):
        self.texto = texto
        self.seila = 'eu iniciei'
        print(self.seila, self.texto)


lista = {'testea': 'teste1', 'teste': 'teste2'}

teste = ImprimirTexto(lista)
