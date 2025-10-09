from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho()
while True:
    resposta = menu(['Acessar Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Fechar Sistema'])
    if resposta == 1:
        #listar conteudo de um arquivo
        lerArquivo(arq)


    elif resposta == 2:
        cabeçalho('Cadastrar Nova Pessoa')
    elif resposta == 3:
        cabeçalho('\033[32mSistema Fechado')
        break
    else:
        print('\033[31mDigite um valor existente')
    sleep(0.5)