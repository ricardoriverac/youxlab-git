soma = conta = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma = numero + soma
    conta = conta + 1
print(f'Você escreveu {conta} e a soma de tudo é {soma}') 