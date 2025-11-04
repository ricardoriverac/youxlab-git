#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    tabuada = int(input('Digite um número para calcular sua tabuada ->'))
    if tabuada < 0:
        break
    for c in range(0,11):
        print(f'{tabuada} x {c} : {tabuada * c}')
print('Fim do programa, você digitou um número negativo.')