#programa que calcula o preço de uma viagem
km = float(input('Digite o tamanho do destino: '))
print(f'R${km*0.50}' if km <= 200 else f'R${km*0.45}')