def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if fim < inicio:
        fim -= 2
        if passo > 0:
            passo *= -1
    for c in range(inicio, fim+1, passo):
        print(f' {c} ', end='')


inicio = int(input('Digite o primeiro valor: '))
fim = int(input('Digite o último valor: '))
passo = int(input('Digite quanto quer pular: '))
contador(inicio,fim,passo)
print()