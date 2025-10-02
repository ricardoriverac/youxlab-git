peso = float(input('Qual é o seu peso (kg)?'))
altura = float(input('Qual é a sua altura (m)?'))
imc = peso / (altura ** 2)
print(f'Essa pessoa tem o IMC de {imc : .1f}')
if imc <18.5:
    print('Seu peso está ABAIXO do normal!')
elif 18.5 <= imc <25:
    print('Seu peso está NORMAL! ')
elif 25 <= imc <30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('CUIDADO!!! Você está em OBESIDADE!')
elif imc >=40:
    print('CUIDADO!!! Você está em OBESIDADE MÓRBIDA!')