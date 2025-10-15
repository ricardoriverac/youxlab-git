#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = str(input('Digite seu nome completo: '))
primeiro_nome = nome.split()
lista_nome = primeiro_nome[0]
ultimo_nome = primeiro_nome[-1]
print(f"O primeiro nome é '{lista_nome}', e o último nome é '{ultimo_nome}'.")