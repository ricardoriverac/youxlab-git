

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo

    
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ')  
            
        
    
    else:
        for c in range(inicio, fim - 1, -passo):
            print(f'{c} ', end='')
            
        print('FIM!')



contador(1, 10, 1)
contador(10, 0, 2)


print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

