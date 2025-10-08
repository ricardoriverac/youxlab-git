# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valor = ''
valores = []

while valor != 'sair':
    valor = str(input('Digite um valor [ou sair para encerrar]: '))

    if valor != 'sair':
        valor = int(valor)
        print(valor)

        if valor not in valores:
            valores.append(valor)
            valores.sort(reverse = True)

if 5 in valores:
            print(f'O valor 5 está na lista. E aparece {valores.count(5)} vezes.')

else:
            print('O valor 5 não está na lista.')
print(valores)
print(f'A quantidade de números digitados foram {len(valores)}')   



