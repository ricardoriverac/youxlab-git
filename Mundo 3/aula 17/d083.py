print('-'*35)
expressao = str(input('Digite uma expressão: '))
pilha = []
for caracter in expressao:
    if caracter == '(':
        pilha.append('(')
    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('-'*35)
    print('A expressão acima, É VÁLIDA!')
    print('-'*35)
else:
    print('-'*35)
    print('A expressão acima, NÃO É VÁLIDA!')
    print('-'*35)
