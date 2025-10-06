expressao = input('Digite uma expressão: ')
abertos = fechados = 0
if expressao.count('(') == expressao.count(')'):
    for posicao, caractere in enumerate(expressao):
        abertos += 1 if caractere == '(' else 0
        fechados += 1 if caractere == ')' else 0
        if fechados > abertos:
            print('expressão invaliada, fechou parenteses antes de abrir.')
            break
        if posicao == (len(expressao)-1):
            print('expressão valida')
else:
    print('expressão invalida!')