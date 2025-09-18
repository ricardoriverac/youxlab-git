valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anosParaPagar = float(input('Digite em quantos anos você pagará: '))
minimo = salario * 30/100
prestacaoMensal = valorCasa / (anosParaPagar * 12)
print(f'A prestação será de {prestacaoMensal}')

if prestacaoMensal <= minimo:
    print('Concedido')
else:
    print('Negado')