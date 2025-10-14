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
        print('Erro em ler o arquivo')
    else:
        cabeçalho('\033[35mPESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>8} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('erro ao abrir arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever dados do arquivo')
        else:
            print(f'\033[32mNovo registro de \033[34m{nome} \033[32madicionado')
            a.close()