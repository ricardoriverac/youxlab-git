# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
while True:
    number = int(input('Digite um número inteiro: '))
    if number == 999:
     print('Você digitou o número 999,chegou ao fim do programa.')
     break
    soma += number
print(f'A soma dos valores é {soma}')