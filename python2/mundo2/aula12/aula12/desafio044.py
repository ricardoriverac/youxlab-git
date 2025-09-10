altura= float(input('Qual sua altura? ').replace('m', ''))
peso= float(input('Qual seu peso?').replace ('kg', ''))
imc = peso/(altura*altura)
print(imc)
if imc<18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print(str('Você está no peso ideal'))
elif 25 <= imc < 30:
    print('Você está acima do peso ideal')
elif 30 <= imc < 40:
    print('Você está obeso')
elif imc >= 40:
    print('Você está com obesidade mórbida')