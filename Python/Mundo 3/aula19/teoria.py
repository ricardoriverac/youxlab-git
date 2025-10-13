#  Curso de Python 3 - Mundo 3: Estruturas Compostas
# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

# LISTAS []
# entrada
# dados=list()
# dados.append('PEDRO')
# dados.append(25)
# print(dados[0]) # PEDRO
# print(dados[1]) # 25
# saida
# dados
# ---------------
# 'PEDRO'   25
# ---------------
#    0       1

# TUPLAS ()

# OBSERVAÇÃO O .APPEND NÃO FUNCIONA NOS DICIONARIOS

# EX.:1°
# DICIONÁRIOS {} # ex.: dados=dict() OU dados={'nome':'PEDRO','idade':25}
# dados=list()
# dados.append('PEDRO')
# dados.append(25)
# print(dados['nome']]) # PEDRO
# print(dados['idade']) # 25
# dados['sexo']='M' # Masculino
# saida
# dados
# ----------------------------
# 'PEDRO'   25      'M'
# -----------------------------
#   nome   idade    sexo

# REMOÇÃO DE ELEMENTOS
# deldados['idade']


# EX.:2°
# filme={'titulo':'Star Wars', 
#        'ano':1977,
#        'diretor':'George Lucas'
# }
# filme1={'titulo':'Avangers', 
#        'ano':2012,
#        'diretor':'Joss whedon'
# }
# filme2={'titulo':'Matrix', 
#        'ano':1999,
#        'diretor':'Wachwski'
# }
# ------------------------------------------
# 'STAR WARS'    1977     'GEORGE LUCAS'
# ------------------------------------------
#   filme         ano           diretor
# print(filme.values()) # pega as informações dentro dos pontilhados
# print(filme.keys) # pega os nomes das informações
# print(filme.items()) # pega os dois


# EX.:3
# filme={'titulo':'Star Wars', 
#        'ano':1977,
#        'diretor':'George Lucas'
# }

# filme1={'titulo':'Avangers', 
#        'ano':2012,
#        'diretor':'Joss whedon'
# }

# filme2={'titulo':'Matrix', 
#        'ano':1999,
#        'diretor':'Wachwski'
# }
# for k, v in filme.items(): # para cada chave e valor no filme no .iteams, eu vou fazer um print
#     print(f'O {k} é {v}')
# locadora=list()
# locadora.append(filme)
# locadora.append(filme1)
# locadora.append(filme2)
# print(locadora[0]['ano']) # 1977
# print(locadora[2]['titulo'])  # matrix

# k = chave
# v = valor
# PODE SER MODIFICADO

filme = dict()
locadora = list()
for c in range(0, 2):
    filme['NF'] = str(input('Nome do Filme: '))
    filme['sigla'] = str(input('Sigla do filme:'))
    locadora.append(filme.copy())
    print(locadora)
for f in locadora:
    for v in f.values():
        print(v, end='  ')
    print()