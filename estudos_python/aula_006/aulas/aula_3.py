#Como verificar tipos primtivos

'''
Para verificar tipos primitivos
é necessario utilizar o "type()"
'''

'''
Para utilizar o "type()" e necessario 
colocar o tipo da variavel no parenteses
'''

#Contexto

tipo_da_variavel = input('ESCREVA ALGO : ')

#Exemplo

mostra_tipo = type(tipo_da_variavel)
print(mostra_tipo)

#Informação adicional

'''
No python você pode demonstrar
informações adicionais sobre 
algum valor de variavel
'''

#Exemplo

print(tipo_da_variavel.isnumeric())

#Tipos de metodos]

'''
.isnumeric = Metodo utilizado para saber se o valor da variavel e um número ou  não

.isalpha = Demonstra se a variavel e letra ou número

.isalnum = Fala se a variavel contem letras e números 

.isupper = Demonstra se o valor da variavel esta em maiusculo

.islower = Detecta se contem somente letras minusculas

.istitle = E quando a palavra contem letras maiusculas e minusculas

.isspace = Detecta se tem somente espaço na variavel 
'''
