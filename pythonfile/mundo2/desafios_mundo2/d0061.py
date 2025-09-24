print('Gerador de PA')
primeiro_termo = float(input('Digite o primeiro termo'))
razao = float(input('Digite o valor da razão'))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} ')
    termo += razao
    cont += 1 
print('Fim')
