import time
kg = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = (kg/altura**2)
print('Calculando o seu imc . . . . ')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com o peso ideal')
elif imc < 30:
    print('Você está sobrepeso')
elif imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')