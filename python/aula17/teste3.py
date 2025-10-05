valores = []
print('Digite um número\n', '-'*20)
while True:
    answer = ' '
    valores.append(input('Digite um valor: '))
    while answer not in 'SN':
        answer = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    print('-'*20, '\nDigite um número\n', '-'*20)
    if answer in 'N':
        break
for c, v in enumerate(valores):
    print(c, v)