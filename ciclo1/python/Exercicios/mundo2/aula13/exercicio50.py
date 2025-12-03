numero1=int(input('Digite um numero inteiro: '))
numero2=int(input('Digite outro numero inteiro: '))
numero3=int(input('Digite outro numero inteiro: '))
numero4=int(input('Digite outro numero inteiro: '))
numero5=int(input('Digite outro numero inteiro: '))
numero6=int(input('Digite outro numero inteiro: '))
lista=[numero1, numero2, numero3, numero4, numero5, numero6]
soma=0
for numero in lista:
    if numero%2==0:
        print(numero)
        soma += numero
print(f" A soma de todos os numero pares sao: {soma}")