#Terminal
print('Inicio:')

criação_de_variavel = {}

c = 0
while True:
    c += 1
    terminal = str(input(f'{c} >>   '))
    
    #Comandos
    if terminal == 'criar_variaveis':
        Digite_o_valor_da_variavel = str(input(f'Valor da variavel >> '))
        criação_de_variavel[c] = Digite_o_valor_da_variavel
    
    if terminal == 'cancelar':
         print('Fim...')
         break
    
    if terminal == 'valores_variaveis':
        print(criação_de_variavel.values())

    if terminal == 'comandos':
        print('''    1 - cancelar
    2 - valores_variaveis
    3 - criar_variaveis''')