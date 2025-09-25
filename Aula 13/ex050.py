soma = 0 
conta = 0
for c in range(1, 7):
    numero = int(input('Digite o {} valor: '.format(c)))
    if numero % 2 == 0:
        soma = soma + numero
        conta = conta + 1
    print(f'Você informou {conta} números  pares e a soma foi {soma}')