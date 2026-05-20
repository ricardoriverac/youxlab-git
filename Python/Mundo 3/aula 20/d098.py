from time import sleep
def contador(inicio, fim, passo):
    print('-'*20)
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} com passo de {passo}: ')
    for n in range(inicio, fim, passo):
        print(n)
        sleep(0.5)



contador(1, 10, 1)
contador(10, 0, -2)
contador(4, 40, 4)

