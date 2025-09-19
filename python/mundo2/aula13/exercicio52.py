numero=int(input('Digite um numero:'))
tot=0
for c in range(1,numero+1):
    print('\033[34M')
    tot+=1
else:
    print('\033[31m') 
print(f'{c}',end='')
print(f'\n\033[m0 numero {numero} foi divisivel {tot} vezes')
if tot==2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')
