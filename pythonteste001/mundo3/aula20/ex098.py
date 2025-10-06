from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i < f:
        contagem = i
        while contagem <= f:
            print(f'{contagem}', end= ' ',flush=True)
            sleep(0.5)
            contagem += p
        print()
    else:
        contagem = i
        while contagem >= f:
            print(f'{contagem}', end= ' ', flush=True)
            sleep(0.5)
            contagem -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('personalise a contagem voce mesmo agora')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
