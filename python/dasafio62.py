primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
print('Os 10 primeiros termos da PA são:')
while contador <= 10:
    print(termo, end=' → ')
    termo += razao
    contador += 1
print('Fim')
