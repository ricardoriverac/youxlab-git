print('BRASILEIRÃO SÉRIE A 2025')
Times= 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Botafogo', 'Bahia', 'Mirassol', 'Fluminense', 'São Paulo', 'Bragantino', 'Ceará SC', 'Vasco da Gama', 'Corinthians', 'Grêmio', 'Internacional', 'Atlético-MG', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife'
print(Times)
print(f'Os 5 primeiros são {Times[0:5]}')
print(f'Os 4 últimos são {Times[-5:]}')
print(f'Times em ordem alfabética: {sorted(Times)}')
colocação= Times.index('Corinthians')
print(f'O Corinthians está na {colocação}ª colocação')