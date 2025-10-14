# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if fim < inicio:
        fim -= 2
        if passo > 0:
            passo *= -1
    for c in range(inicio, fim+1, passo):
        print(f' {c} ', end='')
inicio = int(input('Digite o primeiro valor: '))
fim = int(input('Digite o último valor: '))
passo = int(input('Digite quanto casas você deseja pular: '))
contador(inicio,fim,passo)
print()
