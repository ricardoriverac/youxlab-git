'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada 
valor digitado pelo usuário. O programa será interrompido quando o número solicitado 
for negativo. 
'''

#Resposta

contador = 0
rotacao = True
resultado = 0
digite_numero = int(input('Digite o número que dezeja ver a tabuada: '))

while rotacao == True:
    if digite_numero > 0:
        contador += 1
        resultado = digite_numero * contador
        print(f'{digite_numero} * {contador} = {resultado}')
    if digite_numero < 0:
        print(f'Número {digite_numero} invalido. Esse número deve ser negativo.')
        break

    if contador == 10:
        break