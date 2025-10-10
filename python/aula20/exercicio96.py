def area(l, c):
    a = l*c
    print('-'*30)
    print(f'A área do terreno {l}x{c} foi de {a}m²')
    print('-'*30)
print(f'{"Controle de Terrenos"}\n', '-'*30)
area(l = float(input('Digite a largura(m): ')), c = float(input('Digite o comprimento(m): ')))

