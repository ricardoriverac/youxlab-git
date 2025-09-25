print('Sequencia de fibonacci')
n = int(input('Quantos termos você quer mostrar?: '))
termo = 0
termo2 = 1
print(f'{termo} {termo2}', end='')
cont = 3
while   cont <= n :
    termo3 = termo + termo2
    print(f' {termo3}', end='')
    termo = termo2
    termo2 = termo3
    cont += 1 
print(' FIM')
