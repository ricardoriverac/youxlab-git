def manual(a):
    """manual(a)
       -> Faz a automação da exibição de um help
          :param a: recebe o comando que você deseja verificar o InteractiveHelp"""
    help(a)


biblioteca=''
while True:
    print(f'SISTEMA DE AJUDA')
    biblioteca=str(input('Função ou biblioteca >>>'))
    print(f'ACESSANDO O MANUAL DO COMANDO {biblioteca}')
    if biblioteca.upper() == 'FIM':
        print('ATÉ LOGO')
        break
    else: 
        help(biblioteca)


