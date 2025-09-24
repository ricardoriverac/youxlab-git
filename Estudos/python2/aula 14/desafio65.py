
count=0
soma=0
maior=0
menor= 100000000000
Continuação= str('s')
while Continuação == 's':
    Valores= int(input('Escolha um valor: '))
    NúmerosArmazenados=Valores
    count+=1
    soma=soma + NúmerosArmazenados
    media= soma/count
    if NúmerosArmazenados > maior:
        maior= NúmerosArmazenados
    if NúmerosArmazenados < menor:
        menor=NúmerosArmazenados
    Continuação = str(input('Você quer continuar? [s/n]'))
print(f'Você digitou {count} números e a media foi {media}\n O maior valor foi {maior} e o menor foi {menor}')

