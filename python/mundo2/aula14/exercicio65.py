name='S'
soma=quantidade=media=maior=menor=0
while name in "Ss":
    numero=int(input('Digite um numero: '))
    soma+=numero
    quantidade+=1
    if quantidade==1:
        maior=menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
    name=str(input('Quer continuar? [S/N]'))
media=soma/quantidade
print(f'Você digitou {quantidade} numeros e a media foi {media}')
print(f'O maior valor foi {maior} e o men or foi {menor}')