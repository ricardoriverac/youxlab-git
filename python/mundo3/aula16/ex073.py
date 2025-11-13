#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time São Paulo.


tabela = ('Palmeiras','Flamengo','Cruzeiro','Mirassol','Bahia','Botafogo','Fluminense','São Paulo',
'Atlético-MG','Vasco','Bragantino','Ceará','Corinthians','Grêmio','Internacional','Vitória','Santos',
'Juventude','Fortaleza','Sport')
print('Os 5 primeiros times colocados são')
print(*tabela[0:5])
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print('Os 4 últimos times colocado foi')
print(*tabela[16:])
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('Os times colocados em ordem alfabética')
time_alfabetica = sorted(tabela)
print(*time_alfabetica, sep=', ')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
time_procurado = 'São Paulo'
posicao = tabela.index(time_procurado)
print(f'O time São Paulo está na posição {posicao}')

