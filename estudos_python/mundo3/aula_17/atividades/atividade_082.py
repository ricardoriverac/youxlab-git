'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas 
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

#Resposta

lista_numero = []
lista_numero_par = []
lista_numero_impar = []
while True:
    recebe_numero = int(input('Digite um número: '))
    lista_numero.append(recebe_numero)
    #Logica
    if recebe_numero % 2 == 0:
        lista_numero_par.append(recebe_numero)
    if recebe_numero % 2 != 0:
        lista_numero_impar.append(recebe_numero)
    
    quer_continuar = 'o'
    while quer_continuar not in 'sn':
        quer_continuar = str(input("Quer continuar? [s/n] "))
    if quer_continuar == 'n':
        break
    

    

        
print(f'Lista com TODOS os números: {lista_numero}')
print(f'Lista com todos os números PARES: {lista_numero_par}')
print(f'Lista com todos os números ÍMPARES: {lista_numero_impar}')