#Como utilizar o ".format" é "f"

#.format

''' 
O ".format" pode ser uma forma 
diferente de colocar valores 
de variaveis dentro da string
'''

#Exenplo(contexto)

n1 = float(input('Digite um valor : '))
n2 = float(input('Digite um valor : '))
r = n1 + n2 

#Exemplo
print('A soma de {} com {} e equivalente a {}\n'.format(n1, n2, r))

#f

'''
O "f" pode ser colocado antes de abrir
os parenteses, e ele tem a mesma função
 do ".format", mas o "f" e mais eficiete
'''

#Exemplo
print(f'A soma de {n1} com {n2} e equivalente a {r}\n')
