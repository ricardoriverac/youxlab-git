numero1 = float(input('Digite um número inteiro: '))
numero2 = float(input('Digite o segundo número inteiro: '))
numero3 = float(input('Digite o terceiro número inteiro: '))
numero4 = float(input('Digite o quarto número inteiro: '))
numero5 = float(input('Digite o quinto número inteiro: '))
numero6 = float(input('Digite o sexto número inteiro: '))
numero = numero1, numero2, numero3, numero4, numero5, numero6
soma_pares = 0
for numeros in numero:
    if numeros % 2 == 0:
        soma_pares += numeros
print(f'A soma dos números pares são: {soma_pares}')