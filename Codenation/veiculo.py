class Veiculo:
    def __init__(self):
        self.cor = 'preto'
        self.velocidade = 0
        self.numero_rodas = 0

    def aumentar_velocidade(self, velocidade):
        self.velocidade += velocidade
        print(f'Está rodando a{self.velocidade} km/h')

    def parar(self):
        self.velocidade = 0
        print('parado')

    def buzinar(self):
        print('Biii biiiii')


class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()
        self.cor = 'prata'

    def buzinar(self):
        print('Trrimmm trimmmm')


viuva = Veiculo()
vermelha = Bicicleta()
viuva.buzinar()

print(viuva.numero_rodas)
print(vermelha.numero_rodas)
print(viuva.cor)
print(vermelha.cor)
viuva.buzinar()
vermelha.buzinar()
