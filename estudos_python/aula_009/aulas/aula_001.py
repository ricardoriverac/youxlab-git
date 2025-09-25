#Manipulando texto 

#contexto
frase = 'curso em video python'

#O que é fatiamento de string

'''
Fatiamneto de string seria quando a string e cortada
em letras e armazenadas em micros espaços no seu armazenamenro 
'''

#Exemplo

'''
Sem fatiamento de string :

Bom dia 

Com fatiamento de string ;

[B][o][m][ ][d][i][a]
 1  2  3  4  5  6  7

OBS : ate os espaço entre as palavras e armazenadas

Cada micro espaço de armazenamento contem um número,
e a primeira palavra tera o número 0 para identificar
ela, e conforme as letras forem indo os números almenta
(OBS : isso pode ser expecificado no exemplo acima)


'''

#Como fatiar strimg

'''
Para fatiar string e necessario colocar
a variavel na frente depois utilizar o
couchete, e dentro do couchete devera 
colocar o número de identificação da letra 
'''

#Exemplo

print(frase[3])

'''
isso fara que nó terminal apareça somente a letra escolhida, e mais nada
'''

#Como fazer aparecer varias letras

'''
Para que apareça mais de uma letra o usuario devera utilizar os seguintes comando
'''

#Exemplo

print(frase[0:14])

'''
isso fara que apareca as palavras "bom"

O primeiro número representa em qual letra o computador vai começar a aparecer as letras,
e o ultimo número representa a ultima letra que aparecera no terminal

OBS : Caso for colocar uma frase inteira, e necessario que coloque um número acima
da letra desejada pois o computador iguinora a ultima letra, que acaba não adicionando ela 
junto com as outras
'''

#Colo utilizar o fatiamento de forma diferente

'''
Se o ususario quiser colocar determinadas palavras, mas pulando outra ele devera utilizar o comando da seguinte forma
'''

#exemplo

print(frase[0:21:2])

'''
o outimo algarismo representa em quanto em quanto as palavras serão puladas
'''

#Como usar "[:5]" e "[5:]"

'''
Os " : " antes do número faz que todos os algarismos antes do 5
apareça no terminal
'''
#Exemplo
print(frase[:5])

'''
OS " : " depois do número faz que todos os algarismos depois do 5
apareça no terminal
'''
#Exemplo
print(frase[5:])

#Como utilizar [1::5]

'''
Como não existe o segundo número então aparecera todos os algarismo depois 
do 1, só que vai aparecer pulando de 5 em 5
'''
#Exemplo
print(frase[0::2])

print(frase[:21:2])

print(frase[::2])