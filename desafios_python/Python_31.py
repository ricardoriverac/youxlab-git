distancia = int(input('Qual a distância da viagem? '))
calculo1 = distancia * 0.50
calculo2 = distancia * 0.45
if distancia <=200:
    print('A distância do trageto vai ser de {}Km.' .format(distancia))
    print('O preço da passagem ficará R${:.2f}' .format(calculo1))
else:
    
    print('O preço da passagem ficará R${:.2f}' .format(calculo2))
