'''
 Crie um programa onde o usuário possa digitar vários valores 
 numéricos e cadastre-os em uma lista. Caso o número já exista 
 lá dentro, ele não será adicionado. No final, serão exibidos 
 todos os valores únicos digitados, em ordem crescente. 
'''

#Resposnda
lista_numerica = []

while True:
    recebe_numero = int(input('Digite um número: '))

    if recebe_numero in lista_numerica:
            print('Esse valor já existe!!')
            lista_numerica.remove(recebe_numero)

    elif recebe_numero not in lista_numerica:
            print('Valor sendo adicionado...')
    lista_numerica.append(recebe_numero)
    deseja_continuar = str(input('Deseja continuar[s/n]: ')).lower()
    if deseja_continuar == 'n':
        print('')
        break
    else:
        if deseja_continuar != 's':
            deseja_continuar = str(input('Opição invalida, deseja continuar[s/n]: ').lower())
            if deseja_continuar == 'n':
                break
        
print('LISTA DE NÚMEROS')
print('-=-=-=-=-=-=-=-=-')
lista_numerica.sort()
print(lista_numerica)
    