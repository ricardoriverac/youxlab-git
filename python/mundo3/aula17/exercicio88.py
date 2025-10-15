import random
 
megasena=list()
grupoDeNumeros=list()
resposta=int(input('Quantos jogos você quer? '))


for p in range(resposta):
    for j in range(0,6):
        grupoDeNumeros.append(random.randint(1,60))
    megasena.append(grupoDeNumeros.copy())
    grupoDeNumeros.clear()


for j in range(len(megasena)):
    print(f'Jogo {j+1}: {megasena[j]}')