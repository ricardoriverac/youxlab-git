from random import randint
primeiroNumero = randint (0, 10)
segundoNumero = randint (0, 10)
terceironumero = randint (0, 10)
quartoNumero = randint (0, 10)
quintoNumero = randint (0, 10)
numero = (primeiroNumero,segundoNumero,terceironumero,quartoNumero,quintoNumero)
print(numero)
maior = numero[0]
menor = numero[0]
for numero in numero:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    print(maior,menor)
