soma=0
conta=0
for c in range(0,500,2):
    if c%3==0:
        conta=conta+1
        soma=soma+c
print(f'A soma de todos os {conta} valores solicitados é {soma}')