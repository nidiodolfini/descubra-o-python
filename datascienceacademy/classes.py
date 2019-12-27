class Livro:
    def __init__(self, titulo, isbn):
        # este método vai inicializar cada objeto criado a partir desta classe (acho que é tipo construtor do java)
        # o nome deste metodo é __init__
        # (self) é uma referencia a cada atributo de um objeto criado a partir desta classe (tipo o this do java)
        self.__titulo = titulo  # modifica o acesso ao atributo titulo, que não pode mais ser acessado fora da classe
        self.isbn = isbn
        print('Construtor chamado para criar um objeto da classe')

    def __str__(self):
        return f'O titulo do livro é {self.__titulo} e o ISBN é {self.isbn}'

    def imprime(self):
        print(f'Foi criado um livro: {self.__titulo} e ISBN: {self.isbn}')


livro1 = Livro('O meu pau', 666)

print(livro1)

print(type(livro1))

livro1.imprime()

print(livro1.isbn)

print(hasattr(livro1, 'titulo')) #retorna false pelo atributo está protegido
setattr(livro1, "titulo", "O meu pai")
print(getattr(livro1, "titulo"))


class Aluno:
    __doc__ = """
        Classe de estudo
    """
    # Todos os atributos são privados...
    __Nome = ''
    __Serie = 0
    __Notas = [0, 0, 0, 0]

    def __init__(self, Nome, Serie):
        __doc__ = """
            Instancia da classe Aluno
            Parâmetros
            Nome: String com o nome do aluno
            Serie: Integer com a classe do aluno (1 a 9)
        """
        self.__Nome = Nome
        self.__Serie = Serie

    def imprimeAluno(self):
        print(f'O nome do aluno é {self.__Nome} e a série é {self.__Serie}')


aluno = Aluno('Nidio', 3)
aluno2 = Aluno('Teste', 3)

aluno.imprimeAluno()
aluno2.imprimeAluno()
