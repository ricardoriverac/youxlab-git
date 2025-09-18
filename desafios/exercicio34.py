salario = float(input('Digite o seu salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f}, passa ganhar R${:.2f} agora.'.format(salario, novo))