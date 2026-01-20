#Contexto
lanche = ('lanche', 'limonada', 'pizza', 'pudin')
numeros = (1 , 2 , 1 , 3 , 4 , 5 )

#Como saber quantos elementos tem dentro de uma trupla
'''
Com o comando 'len' você pode saber quantos elementos tem dentro
de uma tupla
'''

#Exemplo
print(len(lanche))

#como mostrar os valores da tupla em ordem alfabetica
'''
Você pode mostrar a tupla no terminal 
em ordem utilizando o comando "sorted"
'''

#Exemplo

print(sorted(lanche))  

#Como contar um valor expecifico dentro de uma tupla

'''
Para conseguir contar um valor específico dentro de 
uma tupla é necessário utilizar o comando "count"
'''

#Exemplo
print("Usando o count:")
print(numeros.count(1))     #saída 2

#Como saber a posição do valor

'''
Para saber a posição de algum valor da tupla e nessario utilizar
a "index", ele mostra a posição do valor dentro de uma tupla
'''

#Exemplo
print(numeros.index(1))

'''
Mas o index só mostra a posição do primeiro valor da variavel, se
tiver outro valor identico ele não mostraria. Para ele mostrar você 
tem que colocar depois do valor desejado qual a posição que ele vai 
começar a procurar
'''

#Exemplo

print(numeros.index(1, 1))

#Como apagar uma tupla

'''
Uma tupla quando ela e apagada ela e apagada por 
inteira. Para apagar uma tupla e necessario utilizar 
o seguindo comando "del".
'''

#Exemplo

del(numeros)

#Como mostrar o maior e o menor numero de uma tupla
numeros = (1 , 2 , 1 , 3 , 4 , 5 )
#mostrar o maior numeor
print(max(numeros))

#mostar  menor numero
print(min(numeros))