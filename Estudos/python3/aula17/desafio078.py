lista= []
count=-1
maior=0
menor=9999
for cont in range (0,5):
    count+=1
    numero= int(input(f'Digite o valor da posição {count}: '))
    lista.append(numero)
    if maior < numero:
        maior=numero
    elif menor > numero:
        menor=numero
print(f'Você digitou os valores {lista}')
print(f'O maior valor inserido na lista é {maior} nas posições {lista.index(maior)} ')
print(f'O menor valor inserido na lista é {menor} nas posições {lista.index(menor)} ')
    
