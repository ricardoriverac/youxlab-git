larg = float(input('Largura da parede: ' ))
alt = float(input('Altura da parede: ' ))
area = larg * alt
tinta = area / 2
print('sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
print('para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))
