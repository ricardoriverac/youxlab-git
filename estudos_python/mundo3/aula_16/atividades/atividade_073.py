'''
 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro 
 de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Cruzeiro.
'''

#Resposta

classificacao_2024 = (
    "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
    "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco",
    "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude",
    "Red Bull Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá"
)

print('''\n20 primeiros colocados da Tabela do Campeonato Brasileiro 
 de Futebol, na ordem de colocação''')

cinco_primeiros_times = (classificacao_2024[:5])
print(f'\nOs 5 primeiros times: {cinco_primeiros_times}')

quatro_ultimos_colocados = (classificacao_2024[16:])
print(f'\nOs 4 ultimos colocados: {quatro_ultimos_colocados}')

times_ordem_alfabetica = sorted(classificacao_2024)
print(f'\nOs times em ordem alfabeticas: {times_ordem_alfabetica}')


print('\nO Cruzeiro esta na 8º posição')