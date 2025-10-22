from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'luislab.txt'

if not arquivoexiste(arq): #Se não estiver criar um arquivo "arq"
    criararquivo(arq) #cria um arquivo "arq"

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo do arquivo.
        lerarquivo(arq)

    elif resposta == 2:
        #Opção de cadastrar uma pessoa nova.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        #Opção de sair do sistema.
        cabecalho('Saindo do sistema... Até Logo!')
        break
    else:
        #Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
