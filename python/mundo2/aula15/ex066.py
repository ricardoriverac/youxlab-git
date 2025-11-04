#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).

number = 0
soma = 0
while number != 999:
    number = int(input('Digite um número inteiro: '))
    if number == 999:
     print('Você digitou o número de parada "999".')
    soma += number
print(f'A soma dos valores é {soma}.')
print('Você chegou ao fim do programa, até a próxima.')