times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Botafogo', 'Mirasol', 'Bahia', 'Fluminense', 'São Paulo', 'Chapecoense', 'Bragantino', 'Grêmio', 'Ceará SC', 'Vaco da Gama', 'Corinthians', 'Atlético-MG', 'Internacional', 'Santos', 'Juventude', 'Ec Vitória', 'Fortaleza', 'Sport Recife')
print(f'os 5 primeiro colocados são {times[0:6]}')
print(f'os 4 ultimos são {times[-4:]}')
print(f'times em ordem alfabética: {sorted(times)}')
print('o Chapecoense está na posição {}'.format(times.index('Chapecoense')))
# print(f'o Chapecoense está na posição {times.index('Chapecoense')}') essa formatação não funciona e por isso usei a outra forma de formatação