from time import sleep
def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=' * 20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += passo
    else:
        cont = início
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= passo
    print('FIM!')
    print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
