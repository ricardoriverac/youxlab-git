print('Gerador de PA')
primeiro_termo = float(input('Digite o primeiro termo'))
razao = float(input('Digite o valor da razão'))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print(f'{termo} ')
    termo += razao
    contador += 1 
print('Fim')
