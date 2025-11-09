from Python_115b.lib.interface import *

def arquivoExiste(nome):
    try:
        atalho = open(nome,'rt')
        atalho.close()
    except FileExistsError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        atalho = open(nome, 'wt+')
        atalho.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')

def lerArquivo(nome):
    try:
        atalho = open(nome, 'rt')
    except:
        print('Erro ao ler a arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(atalho.read())
        
    