'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

#Resposta

digite_um_numero = 0
quantia_repeticao = 0
soma = 0

while digite_um_numero != 999 :
    digite_um_numero = int(input('Digite um número [999 para parar]: ')) 
    quantia_repeticao += 1
    if digite_um_numero != 999 :
        soma += digite_um_numero
print(f'A quantidade de números digitados são {quantia_repeticao} e a soma entres eles e {soma}.')