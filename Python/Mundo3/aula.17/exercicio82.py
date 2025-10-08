lista = []
pares = []
impares = []

while True:
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    resposta = input('quer continuar [S/N] ').upper()
    if resposta == 'N':
        break
print(f'A lista completa é : {lista}')
print(f'Os numeros pares são: {pares}')
print(f'OS numeros impares são: {impares}')
