times = ('Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'São Paulo', 'Athletico-PR', 'Internacional', 'Corinthians', 
          'Bahia', 'Vasco', 'Goiás', 'Atlético-MG', 'Fortaleza', 'Botafogo', 'Ceará', 'Fluminense', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('A: ',times[0:5])
print('B: ',times[-4:])
print('C: ', sorted(times))

for pos, time in enumerate(times):
    if time == 'Chapecoense':
        print(f'D: Posicição do {time} é {pos + 1}º')