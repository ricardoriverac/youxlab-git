def area():
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    area = largura * comprimento
    print(f'A área de um terreno de {largura} de largura e {comprimento} de comprimento é de {area}m².')

print('Controle de Terrenos')
print('-' * 30)

area()
