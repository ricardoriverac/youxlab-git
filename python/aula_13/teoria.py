# como usar o comando "c"
for c in range (1, 6):
    print('Oi, Mundo! ')
print('FIM')

numero = int(input('Digite um numero: '))
for c in range (0, numero):
    print(c)
print('FIM')

# pulando numeros
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(início, fim+1, passo):
    print(c)
print('FIM')
