# # Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# # A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
# # os valores pares sorteados pela função anterior.

import random
def sorteio():
    valores.clear()
    for i in range(5):
        valor = random.randint(1, 100)
        valores.append(valor)    
    print(f"Os números sorteados foram: {valores} ")
def somapar():
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos números foi {soma}")      
valores =[]
sorteio()
somapar()  




