def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é {a}m²')
print(f'{" Digite os dados de seu terreno para ver sua área ":=^54}')
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)