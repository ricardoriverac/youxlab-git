expressao = str(input('Digite uma expressão: '))
contador = 0

for simbolos in expressao:
    if simbolos == '(':
        contador += 1
    elif simbolos == ')':
        contador -= 1
    
    if contador < 0:
        break

if contador == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está invalida')