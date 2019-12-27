class Livro():
    def __init__(self, titulo, isbn):
        # este método vai inicializar cada objeto criado a partir desta classe (acho que é tipo construtor do java)
        # o nome deste metodo é __init__
        # (self) é uma referencia a cada atributo de um objeto criado a partir desta classe (tipo o this do java)
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto da classe')

    def imprime(self):
        print(f'Foi criado um livro: {self.titulo} e ISBN: {self.isbn}')


livro1 = Livro('O meu pau', 666)

print(type(livro1))

livro1.imprime()

print(livro1.titulo)