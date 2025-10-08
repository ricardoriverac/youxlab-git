from lib.interface import *

cabeçalho()
while True:
    resposta = menu(['Acessar Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Fechar Sistema'])
    if resposta == 1:
        cabeçalho('\033[32m1')
    elif resposta == 2:
        cabeçalho('\033[32m2')
    elif resposta == 3:
        cabeçalho('\033[32mSistema Fechado')
        break
    else:
        print('\033[31mDigite um valor existente')