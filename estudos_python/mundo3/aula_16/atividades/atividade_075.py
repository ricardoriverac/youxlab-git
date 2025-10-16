'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

#Resposta

digite_numero = (int(input('Digite um número: ')) , int(input('Digite outro número: ')) ,
                  int(input('Digite mais um número: ')) , int(input('Digite só mais um número: ')))
par = 0
print(f'\nA quantidade de números 9 que apareceu foi {digite_numero.count(9)}')
for r in digite_numero:
    if r == 3:
        print(f'A 1° posição do número 3 foi {digite_numero.index(3)}')
        break
    else: 
        print('Não a nenhum número 3 encontrado.')
        break


for n in digite_numero:
    if n % 2 == 0:
        par +=1
        
        
print(f'A quantidade de número par foi {par}')
