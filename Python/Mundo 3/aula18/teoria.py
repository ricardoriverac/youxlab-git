# Curso Python #17 - Listas (Parte 2)

# 1°lista                     |  DICAS DO ALFREDO
# dados = list()              |   listaPessoas.append(pessoa.copy())
# dados.append('Lais')        |   pessoa.clear()
# dados.append(16)            |  
# print(dados[0])  # LAIS     |  
# print(dados[1])  # 16       |  

# 2°lista                        EXEMPLO PRÁTICO
# pessoas = list()             |    PESSOAS                          | 
# pessoas.append(dados[:])     |-------------------------------------|
#  OBS.: Não funcionou esse có-|'LAIS'!16|'JÚLIA'!17 |'Pablo'!18     |
# digo acima. Mas pode usar.   |  0    1 |  0     1  |   0     1     |           
#                              |-------------------------------------|
#                              |     0        1             2        |

# pessoas = [['LAIS',16], ['JÚLIA',17], ['Pablo',18]]
# print(pessoas[0][0]) # --------------Escolheu a lista 0 e a pessoa 0: LAIS
# print(pessoas[1][1]) # --------------Escolheu a lista 1 e a idade 1:  17
# print(pessoas[2][0]) # --------------Escolheu a lista 2 e a pessoa 0: PABLO
# print(pessoas[1]) # --------------- É escolhido os dois: ['JÚLIA',17]

# PRÁTICA
# dados = list()
# dados.append('Lais')
# dados.append(16)
# informacoes = list()
# informacoes.append(dados[:]) # [:]-----------volta ao normal
# dados[0] = 'JUJUH'
# dados[1] = 15
# informacoes.append(dados[:])
# print(informacoes) 

# dados = [['ANA', 10], ['BRUNA', 32], ['IGOR', 17], ['JÚLIA', 16]]
# for lista in dados:
#     print(lista[0]) # ------deixa em pé e escolhe só os nomes
#     print(lista[1]) # ------deixa em pé e escolhe só as idades
#     print('-'*70)
#     print(f'{lista[0]} tem {lista[1]} anos de idade.')
#     print('-'*70)

dados = list()
dado = list()
totalMaior = totalMenor = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    dados.append(dado[:])
    dado.clear()
print(dados)
for pessoa in dados:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalMenor += 1
print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade.')

