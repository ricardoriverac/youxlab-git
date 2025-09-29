from random import randint
menor = 99999
maior = 0
numero1 = randint(0,10)
numero2 = randint(0,10)
numero3 = randint(0,10)
numero4 = randint(0,10)
numero5 = randint(0,10)
tupla = (numero1,numero2,numero3,numero4,numero5)
for n in tupla:
    if n > maior:
        maior = n
    if n < menor:
        menor = n 
print(f'O menor valor é {menor} e o maior é {maior}')    
print(f'Os valores sorteados foram {tupla}')

