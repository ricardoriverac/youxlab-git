primeiro = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão: '))
termo = primeiro
count = 1 
while count <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    count += 1
    print('\npausa')