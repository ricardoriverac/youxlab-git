peso = float(input('peso: '))
altura = float(input('altura: '))
imc = peso/pow(altura, 2)
print(f'Seu IMC deu {imc}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc < 25:
    print('Peso ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')