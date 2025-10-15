def area():
    comprimento = (float(input('Comprimento: ')))
    largura = (float(input('Largura: ')))
    area = comprimento * largura
    print(f'A área do terreno é de {area} m².')

def cabecalho():
    print()
    print('----- Controle de terreno -----')
    print()


# Programa Principal
cabecalho()
area()