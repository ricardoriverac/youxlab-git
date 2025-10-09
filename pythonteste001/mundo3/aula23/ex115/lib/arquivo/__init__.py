from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro em ler o arquivo')
    else:
        cabeçalho('\033[35mPESSOAS CADASTRADAS')
        print(a.read())


