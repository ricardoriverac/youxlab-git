#Retornando Valores

#Como utilizar o return
'''
A palavra-chave return em Python serve para enviar (retornar) 
um valor de dentro de uma função para fora dela.É a forma que 
uma função tem de entregar um resultado.
'''
#Exemplo 

def soma(a=0, c=0, b=0):
    s = a + c + b
    return s
numeros = soma(2, 4, 6)
print(numeros)