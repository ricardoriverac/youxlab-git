#Tuplas são imutaveis
'''TUPLAS SÃO IMUTAVEIS'''

#Variaveis compostas(tuplas)

'''
Uma "tupla" e uma variavel que guarda mais de 1 valor dentro dela.
Quando um tupla e declarada ela faz um fatiamento 
'''

'''
Para aparecer todos os valores da tupla, só e necesario printar
o nome da tupla
'''
#Exemplo
lanche = ('lanche', 'limonada', 'pizza', 'pudin')
print(lanche)

#Aparecer um valor expecifico da tupla 
'''
Para aparecer um valor expecifico da tupla e necessario
digitar o nome da tubla e entre couchetes colocar o número
que o representa
'''

#Exemplo
print(lanche[3])

#Aparecer um valor expecifico para frente ou para tras
'''
Para aparecer todos os valores depois de um valor expecifico 
em uma tupla, e só colocar um ':' depois do número que 
representa o valor 
'''

'''
Isso também serve para mostra os valores antes 
do valor expecifico, mas inves de colocar os ':' depois 
do número você coloca antes
'''

#Exemplo

#Valores depois do números
print(lanche[2:])

#Valores antes do número
print(lanche[:2])

#Mostra valores expecificos

'''
Para mostra um valor ate outro em tupla, você pode 
colocar o número que representa o primeiro valor 
depois os ':' e em seguida o valor da ultima variavel
'''

#Exemplo
print(lanche[1:3])