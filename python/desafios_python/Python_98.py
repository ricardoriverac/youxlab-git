
def contador(i,f,p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < p:
        conta = 1
        while conta <= f:
            print(f'{conta}', end=' ', flush=False)
            conta += p
        print('FIM')
    else: 
        conta = i 
        while conta >= f:
            print(f'{conta}', end=' ', flush=False)
            conta -= p
        print('FIM')


contador(1,10,1)
contador(10,0,2)
print('Agora e sua vez de personalizar a contagem')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contador(inicio,fim,passo)


