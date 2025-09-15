valorCasa= float(input('Qual o valor da casa? '))
salarioComprador= float(input('Caro cliente, qual o seu salário? '))
anosDeFinanciamento= float(input('Em quantos anos você irá pagar o valor da  casa? '))
parcelaMensalFinanciamento= valorCasa/(anosDeFinanciamento/12)
if parcelaMensalFinanciamento> salarioComprador * 0.30:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido')