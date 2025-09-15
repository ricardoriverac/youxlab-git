distancia = int(input('Qual a distância da viagem? '))
valor = distancia * 0.5
valor2 = distancia * 0.45
if distancia <=200:
    print(f'Você terá que pagar {valor:.2f} por km')
else:
    print(f'Você terá que pagar {valor2:.2f}')