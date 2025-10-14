pilhaAbreParenteses = []
expressao = ''
valido = True

expressao = str(input('Digite a expressão: '))

for i, v in enumerate(expressao):
    if v == '(':
        pilhaAbreParenteses.append('(')

    elif v == ')':
        if len(pilhaAbreParenteses) > 0:
            pilhaAbreParenteses.pop()

        else:
            valido = False
            break

if valido and len(pilhaAbreParenteses) == 0:
    print('A expressão digitada é \033[32mválida\033[m.')
else:
    print('A expressão digitada é \033[31minválida\033[m.')