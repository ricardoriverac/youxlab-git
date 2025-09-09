numero1=int(input('Digite um numero: '))
numero2=int(input('Digite outro numero: '))
numero3=int(input('Digite outro numero: '))

if numero1>numero2:
    if numero1>numero3:
        maior=numero1
    else:
        maior=numero3
else:
    if numero2>numero3:
        maior=numero2
    else:
        maior=numero3

if numero1<numero2:
    if numero1<numero3:
        menor=numero1
    else:
        menor=numero3
else:
    if numero2<numero3:
        menor=numero2
    else:
        menor=numero3        
    print(f"O maior numero é: {maior}")
    print(f"O menor numero é: {menor}")