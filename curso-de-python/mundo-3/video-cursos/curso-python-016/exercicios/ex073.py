tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirasol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo', 'Bragantino', 'Ceara SC', 'Vasco da Gama', 'Corinthians', 'Grémio', 'Atlético-MG', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')

print(f'Os \033[32mprimeiros\033[m 5 colocados são {tabela[:5]}')
print(f'\nOs \033[31múltimos\033[m 4 colocados são {tabela[16:]}')
print(f'\nA lista em ordem alfabética é {sorted(tabela)}')
print(f'\nO Atlético-MG está na {tabela.index("Atlético-MG") + 1}ª posição.')