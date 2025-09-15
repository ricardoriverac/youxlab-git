casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
anosApagar = float(input('Em quantos anos voce vai pagar o valor da casa? '))
valorApagar = casa /(anosApagar/12)
if valorApagar > salario *0.3 :
    print('Emprestimo negado')
else:
    print('Emprestimo APROVADO')