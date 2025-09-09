valor=float(input('Qual o valor da casa?: R$ '))
salario=float(input('Quanto é o seu salário?: R$ '))
anos=int(input('Em quantos anos você vai pagar?: '))
meses=12*anos
prestaçao=valor/meses

if prestaçao<=0.3*salario:
    print(f"Empréstimo aceito!")
else:
    print(f"Empréstimo negado!") 