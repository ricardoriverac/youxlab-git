#from lib.interface import *

#cabeçalho('Testando 123')





#from lib.interface import *

#cabeçalho('SISTEMA ARQUIVO v1.0')





#from lib.interface import *

#menu(['opc01', 'opc02', 'opc03', 'Super opção'])





#from lib.interface import *
#from time import sleep
#while True:
 #   resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
  #  if resposta == 1:
   #     print('Opção 1')
    #elif resposta == 2:
     #   print('Opção 2')
    #elif resposta == 3:
     #   print('Saindo do sistema... Até logo!')
      #  break
    #else: 
     #   print('\033[31mERRO Digite uma opção válida!\033[m')
    #sleep(2)







#from lib.interface import *
#from time import sleep
#while True:
 #   resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
  #  if resposta == 1:
   #     print('Opção 1')
    #elif resposta == 2:
     #   print('Opção 2')
    #elif resposta == 3:
     #   cabeçalho('Saindo do sistema... Até logo!')
      #  break
    #else: 
     #   print('\033[31mERRO Digite uma opção válida!\033[m')
    #sleep(2)






#from lib.interface import *
#from lib.arquivo import *
#from time import sleep

#arq = 'cursoemvídeo.txt'

#if not arquivoExiste(arq):
 #   criarArquivo(arq)

#while True:
    #resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    #if resposta == 1:
     #   cabeçalho('Opção 1')
    #elif resposta == 2:
     #   cabeçalho('Opção 2')
    #elif resposta == 3:
      #  cabeçalho('Saindo do sistema... Até logo!')
     #   break
    #else: 
     #   print('\033[31mERRO! Digite uma opção válida!\033[m')
    #sleep(2)






from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else: 
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)





from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else: 
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
