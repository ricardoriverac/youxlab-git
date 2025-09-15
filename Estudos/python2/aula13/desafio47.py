soma = 0
count=0
for c in range (3, 501, 6):
    divisao= c//2 
    if c  % divisao == 1:    
        soma=soma+c
        count= count+1
print(f'A soma dos {count} valores é {soma}! ')