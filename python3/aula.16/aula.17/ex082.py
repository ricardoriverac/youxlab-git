lista = []
lista2 = []
lista3 = [] 
continuar = 'S'
while continuar == 'S':
    lista.append(int(input('Digite um numero:')))
    print(lista)
    continuar = str(input('Deseja continuar [S/N]:')).upper()
for valor in lista:
    if valor % 2 == 0:
        lista2.append(valor)
    else:
        lista3.append(valor) 
print(f'A lista completa é {lista}')
print(f'Os numeros pares dentro da lista sao {lista2}\nOs valores impares sao {lista3}')    
