dado = []
pessoas = []
continuar = 'S'
menor = maior = 0
while continuar == 'S':
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input('Deseja continuar [S/N]:')).upper()
print(f'Foram cadastradas {len(pessoas)}')
for p in pessoas:
    if p[1] == maior:
        print(f'O maior peso foi {maior}, {p[0]}')            
    if p[1] == menor:
        print(f'O menor peso foi {menor}, {p[0]}')

    

