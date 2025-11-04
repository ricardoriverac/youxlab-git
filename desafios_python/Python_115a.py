from interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    
    sleep(2)




#ENTRA PARTE
def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return numero


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    conta = 1
    for item in lista:
        print(f'\033[33m{conta}\033[m - \033[34m{item}\033[m')
        conta += 1
    print(linha())
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao
