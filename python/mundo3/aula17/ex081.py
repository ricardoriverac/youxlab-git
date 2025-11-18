# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

continuar = 'S'
lista = []
num_procurado = 5
while continuar == 'S':
    num_str = input('Digite um número:' )
    numero =int(num_str)
    lista.append(numero)
    continuar = input('Você deseja continuar:[S/N]').upper()
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'Os números em ordem decrescente são: {lista}')
if num_procurado in lista:
    print('O número "5" foi digitado durante o programa.')
else:
    print('O número "5" não foi digitado durante o programa.')


