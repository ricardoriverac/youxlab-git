salario = float(input("quantos que vc ganha: "))
if salario < 1250:
    aumento = salario * 0.15
    print(f"voce recebeu um aumento de 15%")
else:
    aumento = salario * 0.10
    print(f"voce recebeu um aumento de 10%")    