def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a} m².')


# Programa principal
print('Controle de Terrenos')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)