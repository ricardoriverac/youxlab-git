pesocorporal = float(input('Qual seu peso?:'))
altura = float(input('Qual sua alura?:'))
imc = pesocorporal / (altura ** altura)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <18.5: 
    print('Você está abaixo de peso normal')
elif 18.5 <= imc < 24.9:
    print('Parabéns você está com um bom peso')
elif 25 <= imc < 29.9 :
    print('Você está com sobrepeso')
elif 30 <= imc < 34.9:
    print('Você está com obesidade')
elif imc >= 40:
    print('Você está com obesidade mórbita, cuidaddo')
