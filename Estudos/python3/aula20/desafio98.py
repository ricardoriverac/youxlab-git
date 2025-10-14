import time
def contador(i, m, f):
            print(f'Contagem de {i} até {f} de {m} em {m}:')
            cont=i
            while cont <= f:
                    print(f'{cont} ', end='')
                    cont+=m
            print('fim')

contador(1, 1, 10)
contador(1,2,10)
print('Agora sua vez de personalizar a contagem')
ini= int(input('Escolha o valor inicial da contagem'))
em= int(input('Escolha de quanto em quanto'))
fin= int(input('Escolha o final'))
contador(ini, em, fin)