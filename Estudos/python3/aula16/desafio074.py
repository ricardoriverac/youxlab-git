import random
numero1=random.randint(0,10)
numero2=random.randint(0,10)
numero3=random.randint(0,10)
numero4=random.randint(0,10)
menor=999999
maior=0
seleção= numero1,numero2,numero3,numero4
n=0
for numero in seleção:
    if numero > maior:
        maior=numero
    elif menor > numero:
        menor=numero
print(f'Os valores escolhidos foram {seleção}')
print(f'O maior valor escolhido foi {maior} e o menor valor escolhido foi {menor}')