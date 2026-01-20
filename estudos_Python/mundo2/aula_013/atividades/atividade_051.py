'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressÃO.
'''

#Resposta 
print('10 PRIMEIROS TERMOS')
primeiro_termo = int(input('Digite o Primeiro termo: '))
rasao = int(input('Digite a rasão: '))
decimo_termo = primeiro_termo + (10 - 1) * rasao
for c in  range(primeiro_termo, decimo_termo + rasao, rasao):
    print(c)
print('FIM') 
