'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

#Resposta

digite_um_ano = int(input('Digite o ano que deseja analizar? \n'))


if digite_um_ano % 4 == 0 and digite_um_ano % 100 != 0 or digite_um_ano % 400 == 0 :

        print(f'O ano {digite_um_ano} e BISSEXTO!!')

else :
        
       print(f'O ano {digite_um_ano} não e  BISSEXTO!!')