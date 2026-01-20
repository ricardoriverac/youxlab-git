#Lista(parte1)

#contexto
lista2 = [4, 1, 9, 2, 7, 6, 10, 3, 8, 5]
alimentos = ['Espinafre' , 'Sorvete' , 'Macarrão' , 'Limão']
print(alimentos)


#O que é uma lista
'''
Uma lista e muita simiar a uma tupla, mas uma tupla e imutavel já 
a lista você poe mutar
'''

#Adicionar elementos novos em uma lista

'''
Para adicionar elementos novos em uma lista 
e necessario utilizar o metodo ".append('Alface')
'''
#Exemplo
alface = alimentos.append('Alface')
print(alimentos)

#Como adicionar elementos e qualquer posição dentro da lista
'''
Para adicionar o elemento dentro de uma lista em qual quer 
pisição devera utilizar o metodo ".insert(0 , Queijo)". Para utilizar
o ".insert()" devera colocar dentro do parenteses o número da posição
que deseja que o elemento fique e depois uma virgula ','  e em seguida 
o valor que deseja colocar naquela posição
'''
#Exemplo
queijo = alimentos.insert(3, 'Queijo')
print(alimentos)

#Como apagar elementos dentro de uma lista

'''
Para apagar elementos dentro de uma lista, você pode usar 2 comandos deferentes.
O 1° metodo e o 'pop()'. Para utilizalo você devera colocar o dentro do parentese
o valor da posição do elementos
'''

'''
O 2° metodo e o 'remove()'. Ele e muito similar ao 'pop' mas inves de colocar 
o valor da posição do elementos devera colocar o valor que esta dentro da lista 
que deseja apagar
'''
#Exemplo
#1°
exclui1 = alimentos.pop(3)
#2°
exclui2 = alimentos.remove('Alface')
print(alimentos)

#Criar uma lista com determinados números
'''
Você pode criar uma lista de 4 até 16, e para fazer isso
e necessario fazer os seguintes comandos:
'''
#Exemplo
lista = list(range(4, 16))
print(lista)

#Como deixar a lista em ordem
'''
Para deixar a lista em ordem, você pode usar o metodo "sort()".
Você pode usalo da seguinte forma: 
'''
#Exemplo
lista2.sort()
print(lista2)

#Para deixar a lista organizada de uma forma de tras para frente
'''
Para a lista ficar organizada de tras para frente tera que 
colocar dentro do parenteses os seguintes comandos 'reverse=True'
'''
#Exemplo
lista2.sort(reverse=True)
print(lista2)

#Como saber quantos elementos tem uma lista
'''
para saber a quantidade de elementos dentro de uma lista devera utilizar
o comando 'len()'. Devera colocar o nome da lista que deseja ver a quantidade 
de elementos dentro dos parenteses
'''
#Exemplo
print(len(alimentos))