# importa o sleep pra ter pausa de um número pro outro
from time import sleep
def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} até {fim} com passo de {passo}')
    for n in range(inicio,fim+1,passo):
        print(n)
        sleep(0.5)


contador(1,11,1)   
contador(10,-2,-2)
contador(0,18,3)