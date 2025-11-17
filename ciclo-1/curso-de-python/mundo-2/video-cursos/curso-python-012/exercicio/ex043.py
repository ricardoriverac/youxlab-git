peso = float(input('Digite o seu Kg: '))
altura = float(input('Digite sua altura: '))

imc = (peso / (altura * altura))

print('\033[33m\nCalculando...\033[m\n')

if imc < 18.5:
    print(f'Você pesa {imc:.2f}. Você está abaixo do peso.')

if imc >= 18.5 and imc <= 25:
    print(f'Você pesa {imc:.2f}. Você está no peso ideal.')

if imc >= 25 and imc <= 30:
    print(f'Você pesa {imc:.2f}. Você está em Sobrepeso.')

if imc >= 30 and imc <= 40:
    print(f'Você pesa {imc:.2f}. Você está Obeso.')

if imc > 40:
    print(f'Você pesa {imc:.2f}. Você está em Obesidade mórbida.')