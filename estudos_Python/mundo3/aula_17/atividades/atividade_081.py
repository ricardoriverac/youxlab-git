'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

#Resposta

contador = 0
lista_numerica = []
while True:
    lista_numerica.append(int(input('Digite um número: ')))
    deseja_continuar = str(input('Deseja continuar[s/n]: ')).lower()
    contador += 1
    lista_numerica.sort(reverse=True)
    if deseja_continuar == 'n':
       break
    if deseja_continuar != 's':
        deseja_continuar = str(input(f'Opição invalida. Deseja continuar[s/n]: ')).lower()
    else:
        if deseja_continuar == 'n':
         break

print(f'A quantidade de números digitados foi {contador}')
print(f'A lista dos números digitados: {lista_numerica}')
if 5 in lista_numerica:
    print(f'O número 5 está na lista!!')