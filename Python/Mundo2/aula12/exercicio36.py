valorCasa = float(input('Digite o valor da casa: '))
salario =  float(input('Qual é o seu salario: '))
divida = float(input('Em quantas vezes vai parcelar: '))
anos = float(input('É em quantos anos vai pagar: '))
limite = salario * 0.30
prestacaomensal = divida / anos
if divida <= limite:
    print('\n Emprestimo aprovado! ')
    print(f'A prestação mensal será de: R${prestacaomensal} ')
    print(f'Esta prestação está dentro do limite de 30% do seu salário (R$ {limite}).')
else:
    print('\nEmprestimo negado ! ')
    print(f'O valor da prestação mensal (R${prestacaomensal}, necessita de 30% do seu salario (R${limite}))')