'''
Melhora o DESAFIO 061. perguntando para o usuário se ele quer 
mostrar mais alguns termos. O programa encerra quando ele disser 
que quer mostrar O termos.
'''

#Resposta

import time

razao = int(input('Digite a rasão: '))
termo = int(input('Digite o termo: '))
fim = False
repetir = 0 
repetir2 = 0
print('\nCOMEÇO: ')
while fim == False:
    while repetir != 10:
        print(razao)
        razao += termo
        repetir += 1

    repetir = 1
    if repetir != 0 :
        while repetir != 0:
            repetir = int(input('PAUSA!! Quantos termos que você quer que mostra a mais: '))

            while repetir2 != repetir:
                print(razao)
                razao += termo
                repetir2 += 1
            repetir2 = 0

        if repetir == 0 :
            print('Finalizando programa...')
            time.sleep(1)
            print('Programa finalizado.')
            print('Volte sempre :)')
            fim = True
