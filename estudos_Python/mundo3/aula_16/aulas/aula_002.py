lanche = ('Sorvete' , 'Suco' ,'Pizza' ,'Pudin')

'''O codigo a baixo, fica repetindo, mas toda vez que repetir
ele vai mostrar um valor diferente da tupla, e vai parar de 
repetir quando não tiver mais valores na tupla '''

#Exemplo
for comida in lanche:
    print(f'{comida}')

for cont in range(0, len(lanche)):
    i = int(input(lanche[cont]) )
#Somando tuplas
'''
Quando você soma duas tuplas, você acaba juntando as 
duas tuplas
'''

#Exemplo

numeros = ('1' , '2' , '3' , '4' , '5')
numeros += lanche
print(numeros)