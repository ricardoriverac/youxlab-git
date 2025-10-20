'''
Faça um programa que leia nome e peso de várias 
pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

#Resposta
maior_menor = []
dados = []
dados_segundarios = []
pessoa_cadastradas = 0


while True:
    nome = str(input('Digite o seu nome (FIM para parar: '))
    if nome == "FIM":
        break
    peso = int(input('Digite o peso: '))
    pessoa_cadastradas =+ 1 

    dados.append(nome)
    dados.append(peso)
    dados_segundarios.append(dados[:])
    dados.clear()

    maior_menor.append(peso)
    max_peso = max(maior_menor)
    min_peso = min(maior_menor)
    for c, p in enumerate(dados_segundarios):
        if max_peso == dados_segundarios[-1][1]:
            print(p[-1])
    
print(dados_segundarios)
print(max_peso)
print(min_peso)