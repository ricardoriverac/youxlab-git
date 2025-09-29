salario = float(input("digite seu salario: "))
valor_da_casa = float(input("digite o valor da casa: "))
quantos_anos = int(input(" Em quantos voce vai pagar:  "))
prestaçao = valor_da_casa / (quantos_anos * 12)
limite = salario * 0.30
if prestaçao <= limite:
    print("emprestimo aprovado")
else:
   print("emprestimo negado")     