lista_todos_os_numeros = list()
lista_pares = []
lista_impares = []

resposta='S'
while resposta != 'N':
    numero=int(input('Digite um valor: '))
    lista_todos_os_numeros.append(numero)
    print(lista_todos_os_numeros)
    resposta=str(input('Quer continuar? S/N ')).upper()

for n in lista_todos_os_numeros:
    if n % 2 == 0:
        lista_pares.append(n)
        
    else:
        lista_impares.append(n)
        


    


print(f'Essa lista é dos números impares: {lista_impares}')
print(f'Essa lista é dos números pares: {lista_pares}')
# print(f'A lista digitada foi {lista}')
# print(f'A lista de numeros pares é {lista1}')
# print(f'A lista de numeros impares é {lista2}')
