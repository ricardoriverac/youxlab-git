primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('\nOs 10 primeiros termos da PA são:')
for i in range(10):
    termo = primeiro + i * razao
    print(termo, end=' → ')
print('FIM')
