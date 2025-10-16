import random
numeros =[]
def sorteio():
    numeros.clear()
    for i in range(5):
        numero = random.randint(1,100)
        numeros.append(numero)    
    print(f"numeros sorteados foram: {numeros} ")
def somapar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f"a soma dos numeros foi {soma}")      
sorteio()
somapar()          