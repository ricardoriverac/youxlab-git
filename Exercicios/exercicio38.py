valor1=int(input('Digite um numero: '))
valor2=int(input('Digite outro numero: '))

if valor1>valor2:
    print(f"O numero {valor1} é maior que o numero {valor2}")
elif valor2>valor1:
    print(f"O numero {valor2} é maior que o numero {valor1}")
else:
    print("Não existe valor maior, ambos são iguais!")