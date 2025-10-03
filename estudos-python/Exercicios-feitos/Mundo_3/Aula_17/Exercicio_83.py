expressao = str(input('Digite uma expressão: '))
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print ('Sua expressão esta correta!')
else:
    print ('Sua expressão esta errada!')