from random import randint
numero_aleatorio1 = randint(0,999)
numero_aleatorio2 = randint(0,999)
numero_aleatorio3 = randint(0,999)
numero_aleatorio4 = randint(0,999)
numero_aleatorio5 = randint(0,999)
guarda = (numero_aleatorio1,numero_aleatorio2 , numero_aleatorio3 , numero_aleatorio4 , numero_aleatorio5)
print(guarda)
maior = guarda[0] 
menor = guarda[0]
for numero in guarda:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(menor,maior)            


