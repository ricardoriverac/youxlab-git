'''
Faça um programa que leia uma frase pelo teclado a mostre:
› Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
'''

#Resposta

digite_nome = str(input('Digite o seu nome: ').upper())
contar_o_nome = (digite_nome.count('A'))

primeiro_a = (digite_nome.find('A')+1)
ultimo_a = (digite_nome.rfind('A')+1)

print(f'A quantidade da letra A tem no seu nome: {contar_o_nome}')
print(f'A primeira letra A está na possição: {primeiro_a}')
print(f'A posição da ultima letra A e: {ultimo_a}')