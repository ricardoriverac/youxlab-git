peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura ** 2)
print(f'{imc}')
if imc <18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')