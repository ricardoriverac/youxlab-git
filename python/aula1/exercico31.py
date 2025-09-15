numero=float(input('Digite a distancia da viagem: '))
if numero < 200:
    valor1=numero * 0.50
    print(f'O valor da viagem é de {valor1}')
else:
    valor2=numero * 0.45
    print(f'O valor da viagem é de {valor2}')