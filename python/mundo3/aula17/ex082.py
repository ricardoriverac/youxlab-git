#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


list_pares = []
list_impares = []
list = []
continu = 'S'
while continu == 'S':
    valor = int(input('Digite um número: '))
    list.append(valor)
    continu = input('você deseja continuar:[S/N]').upper()
print(f'NÙMEROS QUE ESTÃO NA LISTA: {list}')
for numero in list:
    if numero % 2 == 0:
        list_pares.append(numero)
print(f'NÙMEROS PARES: {list_pares}')
for num in list:
    if num % 2 != 0:
     list_impares.append(num)
print(f'NÙMEROS ÍMPARES: {list_impares}')


