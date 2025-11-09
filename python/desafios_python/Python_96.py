def area(largura,comprimento):
    area1 = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area1}m²')




print('Controle de Terrenos')
print('-' * 20)
largura1 = float(input('LARGURA (m):'))
comprimento1 = float(input('Comrprimento (m):'))
area(largura1 ,comprimento1)
