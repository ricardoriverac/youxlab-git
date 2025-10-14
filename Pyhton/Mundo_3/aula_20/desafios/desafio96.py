def area():
    # Pede ao usuário o comprimento do terreno
    comprimento = float(input('Comprimento: '))
    
    # Pede ao usuário a largura do terreno
    largura = float(input('Largura: '))
    
    # Calcula a área multiplicando comprimento pela largura
    area = comprimento * largura
    
    # Exibe o resultado da área calculada
    print(f'A área do terreno é de {area}m² quadrados')

def cabecalho():
    # Apenas imprime um cabeçalho para o programa
    print()
    print('----- Controle de terreno -----')
    print()

# ===== Programa Principal =====

cabecalho()  # Chama a função que imprime o cabeçalho
area()       # Chama a função que calcula e mostra a área do terreno
