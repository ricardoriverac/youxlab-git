#programa que calcula o preço de uma viagem
km = float(input('Digite o tamanho do destino: '))
if km < 201:
    print(f'{km*0.50}')
else:
    print(f'{km*0.45}')