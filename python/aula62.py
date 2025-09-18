print('gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razao da PA: '))
termo = primeiro
cont = 1 
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end='')
        termo += razao
        cont += 1
print('pausa')
mais = int(input('quantos termos voce quer mostrar a mais?'))
print('progresao finalizada com {} termos mostrados.'.format(total))
