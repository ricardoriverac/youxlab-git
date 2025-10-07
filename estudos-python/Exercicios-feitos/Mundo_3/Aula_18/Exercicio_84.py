pessoas = []
dados = []
maior = 0
menor = 0
opcao = 'S'
teste = input('')
while opcao == 'S':
    dados.append(input('Insira seu nome: ').strip().capitalize())
    dados.append(int(input('Insira seu peso: ').strip()))
    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados [1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    if len(pessoas) > 2:
        opcao = input('Se você quiser continuar digite S: ').strip().upper()
        
print(f'Foram cadastradas {len(pessoas)} pessoas no sistema!')  
print(f'O maior peso foi de {maior}kg')

for p in pessoas:
    if p[1] == maior:
        print (f'{p[0]}')
        
print(f'E o menor peso foi de {menor}kg')

for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')
print('FIM')