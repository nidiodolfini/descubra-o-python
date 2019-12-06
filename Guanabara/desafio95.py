jogador = dict()
jogadores = list()
gols = list()

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {i + 1}: ")))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    resp = str(input("Quer continuar:"))
    if resp in "nN":
        break

print('-='*30)
print(jogadores)
print('-='*30)
print(f'{"COD":<5}{"Nome":<10}{"gols"}{"total":>15}')
for i, v in enumerate(jogadores):
    print(f'{i:<2} {v["nome"]:<10} {v["gols"]} {v["total"]:>10}')

print('-='*30)
resp = 0
while resp != 999:
    resp = int(input("Mostrar dados de qual jogador (999 para)? "))
    if resp < len(jogadores):
        print(f'Levantamento do jogador: {jogadores[resp]["nome"]}')
        for k, i in enumerate(jogadores[resp]["gols"]):
            print(f'No jogo {k} fez {i} gols')
    elif resp < 999:
        print("Digite um valor valido")


# print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
# for i, v in enumerate(jogador['gols']):
#     print(f'Na partirda {i+1}, fez {v} gols')
# print('-='*30)
# print(f'foi um total de {jogador["total"]} gols')
