largura = float(input('largura da parede :'))
altura = float(input('Altura da parede :'))
area = largura * altura
tinta = area / 2 
print('Para pintar essa parede,voce vai precisar de {}l de tinta' .format(tinta))
print('Sua parede tem dimençao de {} x {} e sua area é de {}m .' .format(altura,largura,area))