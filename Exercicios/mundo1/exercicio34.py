salario=float(input('Qual o valor do seu salário atual?: R$ '))
aumento_superior=salario* 1.10
aumento_inferior=salario* 1.15
if salario>1250.00:
   print(f"O valor com 10% de aumento é: {aumento_superior:.2f}")
else:
   print(f"O valor com 15% de aumento é: {aumento_inferior:.2f}")
