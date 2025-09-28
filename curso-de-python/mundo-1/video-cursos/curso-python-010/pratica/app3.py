numero1 = float(input('Digite a primeira nota: '))
numero2 = float(input('Digite a segunda nota: '))
media = (numero1 + numero2)/2
print(f'A sua média foi {media}')
print('PARABÉNS!' if media >= 6 else 'ESTUDE MAIS!')