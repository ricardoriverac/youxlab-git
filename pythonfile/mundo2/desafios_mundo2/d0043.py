peso = float(input('Qual é o seu peso (Kg): '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura **2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('Você esta abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print('Você esta na média ideal de peso')
elif imc >= 25 and imc < 30:
    print('Você esta sobrepeso')
elif imc <= 30 and imc < 40:
     print('Você esta em obesidade morbida')