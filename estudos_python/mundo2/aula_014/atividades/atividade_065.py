'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário 
se ele quer ou não continuar a digitar valores.
'''

#resposta

#Variaveis
repeticao = False
digite_numero = 0
soma = 0
contador = 0
media = 0 
maior = 0
menor = 1000

while repeticao == False : 
    digite_numero = int(input('Digite um número: '))
    quer_continua = str(input('Quer continuar digitando números[S/N]: ').upper())
    contador += 1

    #Mostrando qual e o maior e o menor número 
    if digite_numero > maior :
        maior = digite_numero
    if digite_numero < menor :
        menor = digite_numero

    #Qualcular a media  
    soma += digite_numero

    if quer_continua == 'S' :
        repeticao == True

media = soma / contador

print(f'''A media de todos os números e {media}.
E o menor número e {menor} e o maior e {maior}.''')