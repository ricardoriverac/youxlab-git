'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

#Resposta

#variaveis
idade = 0 
sexo = 0
pessoa_mais_18 = 0
sexo_masculino = 0
mulher_menos_20 = 0
a = True

#corpo do codigo
while a == True:

    #pergunta qual o sexo e a idade e se deseja continuar
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    idade = int(input('Qual a idade da pessoa: '))
    sexo = str(input('Qual o sexo da pessoa[m/f]: ')).upper()
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    continuar = str(input('\nDeseja continuar[s/n]: ').upper())

    #Logica do codigo 

    if continuar != 'N' or continuar != 'S':
        print('Resposta invalida.')
        continuar = str(input('\nDeseja continuar[s/n]: ').upper())

    #quantas pessoas tem mais de 18
    if idade >= 18:
        pessoa_mais_18 += 1
    
    #quantidade de homens
    if sexo == 'M':
        sexo_masculino += 1

    #quantas mulheres tem menos de 20 anos 
    if sexo == 'F' and idade < 20:
        mulher_menos_20 =+ 1


    if continuar == 'N':
        break

#Mostra todas as informações da logicas do codigo no terminal
print(f'A quantidade de pessoas com mais de 18 anos e {pessoa_mais_18}.')
print(f'A quantidade de Homens foram cadastrados foi {sexo_masculino}.')
print(f'A quantia de mulheres com menos de 20 anos e {mulher_menos_20}.')