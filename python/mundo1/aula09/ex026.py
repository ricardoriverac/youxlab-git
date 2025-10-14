#Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que
# posição ela aparece a última vez.

frase = str(input('Digite uma frase: '))
letra_busca = 'a'
primeira_posi = frase.find(letra_busca)
ultima_posi = frase.rfind(letra_busca)
if primeira_posi != -1:
    print(f"A primeira posição da letra {letra_busca} é: {primeira_posi}")
else:
    print(f"A letra '{letra_busca}' não foi encontrada!")

if ultima_posi != -1:
    print(f"A útima posiçaõ da letra {letra_busca} é: {ultima_posi}")
else:
    print(f"A letra '{letra_busca} não foi encontrada.")



