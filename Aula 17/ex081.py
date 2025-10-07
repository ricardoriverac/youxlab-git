numero = []
while True:
    numero.append(int(input('informe um valor para que possamos ler: ')))
    valor = str(input('Deseja continuar? [S/N] '))
    if valor in 'Nn':
        break
print('=' * 50)
print(f'Vc colocou {len(numero)} valores: ')
numero.sort(reverse=True)
print('Os numeros em ordem decrescente são{}'.format(numero))
if 5 in numero:
    print('O numero 5 está na lista ')
else: 
    print('O numero 5 não está na lista')