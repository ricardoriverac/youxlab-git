times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio', 'Fluminense',
         'Athletico-PR', 'São Paulo', 'Internacional', 'Cruzeiro', 'Fortaleza',
         'Corinthians', 'Bahia', 'Vasco', 'Santos', 'Cuiabá',
         'América-MG', 'Bragantino', 'Goiás', 'Coritiba', 'Chapecoense')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
