largura = int(input('Largura da parede'))
altura = int(input('Altura da parede'))
área = altura*largura
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {área}m²')
tinta = área/2
print(f'Para pintar toda sua área você precisará de {tinta}L por m²')
