#imports e funções

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

#código principal
valores =[]
sorteio()
somapar()