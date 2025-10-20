'''
 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo 
 deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

#Responda

#vatriaveis
quantidade_parenteses_direita = 0
quantidade_parenteses_esquerda = 0

#verifica a quantidade de '('
lista_expessão = input('Digite quantidade_parenteses_esquerda   expressão númerica: ')
n2 = (' '.join(lista_expessão))
n1 = (n2.split())
for c, v in enumerate(n1):
    if v == '(':
        quantidade_parenteses_esquerda += 1

#verifica a quantidade de ')'
n3 = (' '.join(lista_expessão))
n4 = (n3.split())
for c, v in enumerate(n1):
    if v == ')':
        quantidade_parenteses_direita += 1

#mostra se a expressão e valida ou não
if quantidade_parenteses_esquerda   == quantidade_parenteses_direita:
    print('A sua expressão e VALIDA!!')
else:
    print('A sua expressão  NÃO e VALIDA!!')