expressoes = input('Digite uma expressão matemática qualquer: ')
aberto = 0
fechado = 0
if expressoes.count('(') == expressoes.count(')'):
    for posicao, caractere in enumerate(expressoes):
        aberto = aberto + 1 if caractere == '(' else 0
        fechado = fechado + 1 if caractere == ')' else 0
        if fechado > aberto:
            print('Essa expressão é invaliada ! :( )')
            break
        if posicao == (len(expressoes)-1):
            print('Essa expressão é valida ! :D')
else:
    print('expressão invalida!')