soma=0
conta=0
for c in range(1,8):
    num=int(input(f'Digite o {c} valor: '))
    if num%2==0:
        soma+=num
        conta+=1
print(f'Voce informou {conta} numeros PARES e a soma foi {soma}')
        