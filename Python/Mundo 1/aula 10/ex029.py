velocidadeCarro = int(input('Digite a velocidade do seu carro: '))
custo = 7.0
if velocidadeCarro >= 80: 
    print('Você foi MULTADO!')
    multa = (velocidadeCarro - 80) * custo
    print(f'Você terá que pagar R${multa:.2f} reais')
else:
    print('Você esta aprovado!')
