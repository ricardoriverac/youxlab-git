'''
Crie um programa que leia dois valores e mostre um menu como a baixo:
Seu programa deverá realizar a operação solicitada em cada caso.

[1] somar
[2] multiplicar
[3] mostrar o número maior
[4] novos números
[5] sair do programa
'''

#Resposta

#Biblioteca
import time

#Variaveis
cancela_o_programa = False
numero1 = float(input('Digite o 1° número: '))
numero2 = float(input('Digite o 2° número: '))

#Base do programa
while cancela_o_programa == False :
    #Menu
    print('''

        DIGITE UMA DAS OPÇÕES ABAIXO
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=     
        [1] somar
        [2] multiplicar
        [3] mostrar o número maior
        [4] novos números
        [5] sair do programa
    ''')

    #Escolhe as opições do menu
    digite_a_sua_escolha = int(input('Digite um dos números que representa uma escolha acima: '))

    #Codigo da opição 1
    if digite_a_sua_escolha == 1 :
        soma_dos_numeros = numero1 + numero2
        print(f'A soma de {numero1} e {numero2} e igual a {soma_dos_numeros}.')

    #Codigo da opição 2
    if digite_a_sua_escolha == 2 :
        multiplicacao = numero1 * numero2 
        print(f'A multiplicação de {numero1} e {numero2} e igual a {multiplicacao}')

        
    #Codigo da opição 3 
    if digite_a_sua_escolha == 3 :
        if numero1 < numero2 :
            print(f'O maior número e {numero2} e o menor número e {numero1}')
        elif numero2 < numero1 :
            print(f'O maior número e {numero1} e o menor número e {numero2}')

    #Codigo da opição 4 
    if digite_a_sua_escolha == 4 :
        numero1 = float(input('Digite o 1° número: '))
        numero2 = float(input('Digite o 2° número: '))
    
    #Codigo da opição 5
    if digite_a_sua_escolha == 5 :
        print('Finalizando programa...')
        time.sleep(1)
        print('Programa finalizado.')
        print('Volte sempre :)')
        cancela_o_programa = True

    #Codigo da opição não registrada do menu
    if digite_a_sua_escolha != 1 or digite_a_sua_escolha != 2 or digite_a_sua_escolha != 3 or digite_a_sua_escolha != 4 or digite_a_sua_escolha != 5 :
        print('Essa opição não existe. Escolha outra no menu abaixo.')
