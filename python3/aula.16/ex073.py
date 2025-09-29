colocados = ('Flamengo','Cruzeiro','Palmeiras','Mirassol','Botafogo','Bahia','São Paulo',
'Fluminense','Bragantino','Grêmio','Vasco','Corinthians','Ceará','Atlético-MG','Internacional',
'Santos','Juventude,Vitória','Fortaleza','Sport')
print(f'Os primeiros 5 colocados sao {colocados[0:6]}')
print(f'Os ultimos 4 colocados sao {colocados[-4:]}')
print(sorted(colocados))
print(colocados.index('Vasco'))