from time  import sleep

def contagem(comeco, fim, passos):
    print(f'Contagem do {comeco} ao {fim} de {passos} em {passos}')
    sleep(2)

    if comeco < fim:
        count = comeco
        while count <= fim:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count += passos

    else:
        count = comeco
        while count >= fim:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count -= passos

#Código Principal
print('-' * 35)
contagem(1, 10, 1)
print()
print('-' * 35)

contagem(10, 0, 2)
print()
print('-'  * 35)

print('Agora faça sua contagem personalizada!')
comecoUsuario = int(input('Começo: '))
fimUsuario = int(input('Fim: '))
passosUsuario = int(input('Passos: '))

contagem(comecoUsuario, fimUsuario, passosUsuario)
print()
print('-'  * 35)