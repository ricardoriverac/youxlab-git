import random

numeros = []

def sorteia():
    print("Escolhando 5 numeros")
    for i in range(5):
        valor_sorteados = random.randint(1,10)
        numeros.append(valor_sorteados)
        print(f'Os numeros sorteados são {valor_sorteados}', end=" ")
        print(f"{numeros}")

def somaPar():
    soma = 0
    pares = []
    print("somando os pares")
    for i in numeros:
       if i %2 == 0:
        soma += i
        pares.append(i)
        
    if pares:
        print(f"Os pares encontrados foram: {pares}")
        print(f"A soma de todos os pares é: {soma}")
    else:
        print(f"Não contém valores pares!")
        
sorteia()
somaPar()
