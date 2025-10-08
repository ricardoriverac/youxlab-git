lista=list()
expressao=str(input('Digite a expressão: '))
lista.append(expressao)
contadorParenteses= expressao.count('(')
contadorParenteses2= expressao.count(')')
if contadorParenteses ==  contadorParenteses2:
    print('Expressão numérica válida! ')
else:
    print('Expressão numérica inválida!')