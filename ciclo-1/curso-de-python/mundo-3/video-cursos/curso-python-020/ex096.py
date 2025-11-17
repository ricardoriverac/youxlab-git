def area(a, b):
    return print(f'A área do terreno é {a} x {b} é {a * b:.0f}m².')

largura = float(input('Digite a LARGURA(m) do terreno: '))
comprimento = float(input('Digite o COMPRIMENTO(m) do terreno: '))
somaTerreno = area(largura, comprimento)

print(somaTerreno)