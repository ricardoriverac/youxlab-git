def fatorial(numero, show=False):
    fat = 1
    for n in range(numero,0,-1):
        fat=fat*n
        if show==True:
            print(f'{n} ',end='')
            if n > 1:
                print('x ', end='')
            else:
                print(f'= ', end='')
    return fat
    
resultado = fatorial(8,True)

print(resultado)
        
        
        




