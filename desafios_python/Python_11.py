larguradaparede = float(input('Largura da parede:'))
alturadaparede = float(input('Altura da parede:'))
area = larguradaparede * alturadaparede
print(f'Sua parede tem a dimensão de {larguradaparede} x {alturadaparede} e sua área é de {area}m²')
tinta = area / 2
print(f'Para pintar essa parede você precisa de {tinta:.2}l de tinta.')