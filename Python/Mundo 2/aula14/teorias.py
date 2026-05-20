variavel = 1
while variavel < 10:
    print(variavel)
    variavel += 1
print('Fim')

numero = 1
while numero != 0:
    numero = int(input('Digite um valor: '))
print('FIM')

resposta = 'S'
while resposta == 'S':
    valor = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))
    if numero != 0:
       if numero % 2 == 0:
        par += 1
       else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')