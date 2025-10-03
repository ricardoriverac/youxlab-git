valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar?[S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
print(f'{len(valores)} valores digitados')
valores.sort(reverse=True)
print(f'os Valores em ordem decrescente são {valores}')
if 5 in valores:
    print('o valor 5 está presente nessa lista')
else:
    print('O valor 5 não foi encontrado nessa lista')