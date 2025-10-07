listaValor = []
continuar = 's'

while continuar == 's':
    numero = int(input('digite um numero: '))
    if numero in listaValor:
        numero = int(input('esse numero ja foi adicionado. adicione outro: '))
        listaValor.append(numero)
    else:
        listaValor.append(numero)
        print(listaValor)
        continuar = str