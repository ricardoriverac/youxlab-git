lista=list()
expressao=str(input('Digite a expressão: '))
lista.append(expressao)
contadorParenteses= expressao.count('(')
contadorParenteses2= expressao.count(')')
if contadorParenteses % 2 == 0 and contadorParenteses % 2 == 0:
    print('Expressão numérica válida! ')
elif contadorParenteses % 2 != 0 and contadorParenteses2 % 2 != 0:
    print('Expressão numérica inválida!')