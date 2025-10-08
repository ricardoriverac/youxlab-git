print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print(f'{termo} > ' , end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos vc quer mostrar a mais ? '))
print(f'Progressão finalizada com {total} termos mostrados.')