#Variaveis compostas(Dicionarios)
'''
O dicionários são estruturas de dados semelhantes as tuplas e listas, só que 
você consegue personalizar os indices
'''

#Para que serve um Dicionário
'''
O dicionário serve para ter um indice literal. Que ao inves de 
0, 1, 2 ou 3, você pode colocar nomes como indice
'''

#Como declara um dicionário
'''
Para declarar um dicionário, e necessario utilizar os '{}'(chaves). Você pode declarar 
os dicionários de 2 maneiras. A 1° e utilizando o comando 'dict()' e o outro utilizando 
as '{}' 
'''
#Exemplo
#1° forma
dicionario = dict()
#2° forma
dicionari0 = {}

#Como adicionar valores dentro do dicionário
'''
Para adicionar valores detro de dicionários você deve colocar 
dentro das '{}' (chaves) uma aspas simples (''), dentro dessas 
aspas simples você vai colocar o nome da indice. E depois devera 
colocar dois ponto ( : ), e em seguida o valor da indece
(A primeira aspas e o nome da indece, e a segunda o valor da indece, e entre elas vai os ' : ')
'''
#Exemplo
dicionario = { 'Nome':'Pedro' , 'Idade':'18'}

#Adicionar uma nova indece
'''
Para adicionar um indice novo, você deverar colocar o 
nome do dicionário que deseja emplementar uma nova indice,
e em seguida um "[]", e dentro desses "[]" você coloca dentro de 
aspas simples o nome da indece, e depois do "=" coloca o valor
'''
#Exemplo
dicionario['Sexo'] = 'M'

#Como eliminar algum elemento
'''
Para eliminar algum elemento, você pode usar o comando "del".
Para utilizar, devera colocar o nome do dicionário e depois entre "[]"
o nome da indece
'''
#Exemplos
del dicionario['Idade']



