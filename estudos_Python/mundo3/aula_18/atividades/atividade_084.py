'''
Faça um programa que leia nome e peso de várias 
pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

#Resposta
maior_menor = [] #armazena os pesos digitados
dados = [] #usar tuplas 
dados_segundarios = []
pessoa_cadastradas = 0 #com tuplas ha outra forma de fazer
lista_nome_maior_peso = []
lista_nome_menor_peso = []


while True:
    nome = str(input('Digite o seu nome (FIM para parar): '))
    if nome == "FIM":
        break
    peso = int(input('Digite o peso: '))
    pessoa_cadastradas =+ 1 #e o melhor lugar para incrementar?

    dados.append(nome)
    dados.append(peso)
    dados_segundarios.append(dados[:])   
    dados.clear()

    maior_menor.append(peso)
    max_peso = max(maior_menor)
    min_peso = min(maior_menor)
    lista_nome_maior_peso.clear()
    for cadastro in dados_segundarios:
        print(cadastro)
        if max_peso == cadastro[-1]:
            nome_maior_peso = cadastro[0]
            lista_nome_maior_peso.append(nome_maior_peso)

    lista_nome_menor_peso.clear()
    for cadastro in dados_segundarios :
        if min_peso == cadastro[-1]:
            nome_menor_peso = cadastro[0]
            lista_nome_menor_peso.append(nome_menor_peso)
    
print(f'A quantidade de pessoas cadastradas foi: {pessoa_cadastradas}')
print(f'O maior peso e {max_peso}, e as pessoas com esse peso  são: {lista_nome_maior_peso}')
print(f'O menor peso e {min_peso}, e as pessoas com esse peso  são: {lista_nome_menor_peso}')