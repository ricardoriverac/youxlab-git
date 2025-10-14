def área():
    larg = float(input('Largura:(m) '))
    comp = float(input('Comprimento:(m) '))
    tot = larg*comp
    print(f'A Área de um terreno {larg:.1f} x {comp:.1f} é de {tot:.1f}m²')


print('Controle de Terrenos')
print('=*='*7)
área()