'''
Malhora o DESAFIO 061. perguntando para o usuário se ele quer 
mostrar mais alguns termos. O programa encerra quando ele disser 
que quer mostrar O termos.
'''

#Resposta 

import time

rasao = int(input('Digite a rasão: '))
termo = int(input('Digite o termo: '))
fim = False
repetir = 0 
print('\nCOMEÇO: ')
while fim == False:
    print(rasao)
    rasao += termo
    repetir += 1

    if repetir == 10 :
        pausa = int(input('PAUSA!! Quantos termos que você quer que mostra a mais: '))

        if pausa == 0 :
            print('Finalizando programa...')
            time.sleep(1)
            print('Programa finalizado.')
            print('Volte sempre :)')
            fim = True
