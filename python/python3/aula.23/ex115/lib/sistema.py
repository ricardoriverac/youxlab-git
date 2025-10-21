from ex115.lib.interface import *
from ex115.lib.arquivo import *
arq = 'agathalab.txt'

  

while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
  if resposta ==  1:

   print('Opção 1')

  elif resposta == 2:
   print('Opção 2')

  elif resposta == 3:
    print('Saindo do sistema... Até logo!')
    break

  else:
     print('ERRO, digite uma opcao valida')