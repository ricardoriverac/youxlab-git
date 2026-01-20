'''
Rafaça o DESAFIO 051, lendo o primeiro termo a a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

#Resposta

rasao = int(input('Digite a rasão: '))
termo = int(input('Digite o termo: '))
repetir = 0 
print('\nCOMEÇO: ')
while repetir != 10 :
    print(rasao)
    rasao += termo
    repetir += 1 
print('FIM!!')