primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão de Progressão Aritmética: '))
termo = primeiro_termo
contador = 1
while contador <=10:
    print(f'{termo} - ', end='')
    termo += razao
    contador += 1
print('FIM!')