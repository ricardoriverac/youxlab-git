peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
if imc <= 18.5:
    print(f'{imc:.2f}, você está ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print(f'{imc:.2f}, você está com o PESO IDEAL!')
elif 25 < imc <= 30:
    print(f'{imc:.2f}, você está com SOBREPESO!')
elif 30 < imc <= 40:
    print(f'{imc:.2f}, você está com OBESIDADE!')
elif imc > 40:
    print(f'{imc:.2f}, você está com OBESIDADE MÓRBIDA!')
