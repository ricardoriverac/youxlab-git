from modulos.interface import *
from modulos.arquivo import *
from time import sleep

# Nome do arquivo onde os dados ficarão salvos
arq = 'pessoas.txt'

# Verifica se o arquivo já existe, senão cria
if not arquivo_existe(arq):
    criar_arquivo(arq)

# Loop principal do menu
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        # Ver pessoas cadastradas
        ler_arquivo(arq)
    elif resposta == 2:
        # Cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar_pessoa(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')

    sleep(2)
